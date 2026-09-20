# Ferry — Plateforme MLOps 100 % Locale (README détaillé)

> Documentation complète du code source de **Ferry** (répertoire `mlops-platform-spec`) :
> description, outils, fonctionnement et procédure de test. Complète la
> [README principale](./README.md).
>
> **⚠️ ALL-LOCAL** : depuis la refonte, Ferry est une plateforme **entièrement locale** —
> aucune dépendance cloud, aucun fournisseur, aucune API propriétaire. L'infrastructure
> (réseau, volumes, Postgres, MLflow) est provisionnée en local via Terraform (provider
> Docker), l'inventaire Ansible pointe tout sur `127.0.0.1` en connexion locale, et
> Prometheus/Grafana ne scrapent que des cibles loopback. L'ancienne variante multi-cloud
> (GCP + OCI + DORA + portability contract) a été **supprimée**.

---

## 1. Vue d'ensemble

Ferry est un pipeline ML complet (train → track → serve → monitor) qui tourne
**localement**, sans cloud. Le but : démontrer le cycle de vie MLOps avec des composants
auto-hébergés et provider-neutres — c'est la même stack qu'une équipe on-premise ou air-gapped
utiliserait.

**Le promesse tenable de Ferry** :

> Tout — orchestration, tracking, serving, monitoring, CI/CD — tourne sur des ressources
> locales. Aucune compte cloud, aucun service managé, aucune API propriétaire.

### Ce que contient réellement le code

Un pipeline crédit (RandomForest/GradientBoosting sur German Credit Data) servi par FastAPI,
avec : Terraform local (provider Docker), Ansible (roles kubernetes/mlflow/monitoring/
training, inventaire local), Kubernetes (déploiement churn), Prometheus/Grafana, k6, Jenkins,
une suite de tests pytest, et une UI de dashboard.

---

## 2. Stack technique et rôle de chaque outil

| Domaine | Outil | Rôle |
|---|---|---|
| Infrastructure-as-Code | **Terraform** (provider Docker) | Réseau local, volumes, Postgres, MLflow |
| Config management | **Ansible** (connection local) | Roles idempotents (common, docker, kubernetes, mlflow, monitoring, training) |
| Conteneurs | **Docker (+ Compose)** | Stack locale (Postgres, MLflow, train, API) |
| Orchestration | **Kubernetes** (kubeadm self-managed) | Namespace `mlops`, deployment `churn-api`, HPA |
| CI/CD | **Jenkins** | Pipeline : test → train → build → push → deploy |
| Tracking/Registry | **MLflow** (2.10) | Log runs + registry model (churn-model) |
| Serving | **FastAPI + Uvicorn** | `/health`, `/predict`, `/history`, `/stats`, `/model-info` |
| DB | **PostgreSQL** + SQLAlchemy | Table `predictions` (ou SQLite fallback) |
| Metrics | **Prometheus + Grafana** | node_exporter, dashboards API (cibles loopback) |
| Load test | **k6** | 20 VUs, 2 min, seuils p95<1000ms + rate<0.01 |
| ML | **scikit-learn** | GradientBoosting (crédit), churn RF |

---

## 3. Structure du dépôt (détaillée)

```
ferry/  (mlops-platform-spec/)
├── api/
│   ├── main.py                 # FastAPI crédit (train au startup sur German Credit Data)
│   ├── model.py                # chargement modèle depuis MLflow registry
│   ├── schemas.py              # Pydantic v2 : PredictRequest (20 champs), literals A-codes
│   ├── db.py                   # SQLAlchemy : model Prediction + get_database_url (Postgres/SQLite)
│   └── requirements.txt
├── ml/
│   ├── train.py                # GradientBoosting + MLflow, transition Staging
│   ├── evaluate.py             # gate AUC ≥ 0.75 / F1 ≥ 0.30 (exit discret = CI gate)
│   ├── preprocess.py           # ColumnTransformer (OneHot + StandardScaler) partagé
│   ├── generate_churn_data.py  # ~7000 lignes churn
│   └── data/
│       ├── generate_credit_data.py  # parse UCI German Credit Data
│       ├── generate_fraud_data.py   # 100K transactions fraude (~10%)
│       └── churn.csv, credit.csv, fraud.csv
├── tests/
│   ├── conftest.py             # sys.path bootstrap (repo root, api/, ml/, tests/)
│   ├── _data.py                # données German Credit synthétiques
│   ├── test_api.py             # /health, /predict (200 valid, 422), history/stats
│   ├── test_schemas.py         # validation Pydantic (valide/rejet/invalide/borne)
│   ├── test_evaluate.py        # vérifie seuils AUC/F1
│   ├── test_train_pipeline.py  # train→register→artifact (tmp mlruns)
│   └── QA-REPORT.md            # bugs trouvés lors du QA
├── terraform/
│   ├── main.tf                 # ALL-LOCAL : provider Docker (réseau, volumes, Postgres, MLflow)
│   ├── variables.tf
│   └── outputs.tf
├── kubernetes/
│   ├── namespace.yaml, configmap.yaml
│   ├── api/ (deployment, service, ingress, hpa)
│   └── database/ (statefulset, pvc, service, init-configmap)
├── ansible/
│   ├── inventory/hosts.yml     # tout → 127.0.0.1, ansible_connection: local
│   ├── playbooks/ (site, ml, k8s, monitoring)
│   └── roles/ (common, docker, kubernetes, mlflow, monitoring, training)
├── monitoring/
│   ├── prometheus.yml, grafana/dashboards/ml-api-dashboard.json, k6/loadtest.js
├── docker/compose.local.yml    # Postgres + MLflow + train + api
├── docker/api/Dockerfile
├── jenkins/Jenkinsfile
├── ui/index.html               # dashboard "Credit Risk"
└── docs/ (PRD.md, architecture.md, deployment.md)
```

---

## 4. Fonctionnement pas à pas

### 4.1 Données

- `ml/data/generate_credit_data.py` : parse German Credit Data UCI → `credit.csv` (1000 lg,
  20 features + cible). Target `2→1` = défaut.
- `ml/generate_churn_data.py` : churn télécom ~7000 lg (tenure, charges, contract, payment).
- `ml/data/generate_fraud_data.py` : 100K transactions fraude (~10%, montants log-normaux).

### 4.2 Preprocessing & entraînement

- `ml/preprocess.py` : `FEATURE_COLS` (20), `CATEGORICAL_COLS` (13), `NUMERIC_COLS` (7).
  `ColumnTransformer` OneHotEncoder + StandardScaler (mis en cache `_preprocessor`). Expose
  `encode_features`, `apply_encoders` (inférence), `train_test_split` stratifié, `get_feature_names`.
- `ml/train.py` : `GradientBoostingClassifier` (300 estimators, max_depth 6, lr 0.05,
  subsample 0.8). Log MLflow + transition **Staging** + save `model.pkl`.

### 4.3 Évaluation gate (CI)

`ml/evaluate.py` : charge le modèle enregistré, encode, calcule AUC/F1/precision/recall
sur le split de test. **Exit 0 si AUC≥0.75 et F1≥0.30, sinon exit 1** (fait échouer Jenkins).

### 4.4 API (FastAPI, `api/main.py`)

- `risk_tier(prob)` → low/medium/high/critical (0.1/0.3/0.6).
- `train_model()` entraîne au démarrage (`lifespan`) sur German Credit Data.
- Endpoints : `/health`, `/predict`, `/history` (in-memory, max 500), `/stats`,
  `/model-info`, `/` (sert `ui/index.html`), mount `/ui`.
- `api/db.py` : persistance SQLAlchemy optionnelle (Postgres via env, fallback SQLite).
- `api/model.py` : chemin alternatif — chargement depuis **MLflow registry** (`load_model`,
  `get_latest_versions` Production/Staging/None).

### 4.5 Infrastructure (Terraform local)

- `terraform/main.tf` : provider `kreuzwerker/docker` sur le daemon local.
- Réseau `mlops-local-net`, volumes `mlops-local-pg-data` + `mlops-local-mlflow-artifacts`.
- Conteneurs `mlops-local-postgres` (postgres:16, healthcheck pg_isready) et
  `mlops-local-mlflow` (backend Postgres, artifact-root local `/opt/mlflow/artifacts`).
- Aucun cloud, aucune credentials, aucun remote state.

### 4.6 Configuration (Ansible, ALL-LOCAL)

- Inventaire : chaque hôte logique → `127.0.0.1`, `ansible_connection: local`.
- `common` : timezone UTC, packages, node_exporter + UFW (ports 22/9100/5000/9090/3000).
- `docker` : Docker CE, cgroupdriver systemd, log max-size 10m.
- `kubernetes` : swap off, kernel modules, kubeadm 1.28, Calico CNI, join workers, wait Ready.
- `mlflow` : serveur MLflow :5000, artifact-root disque local.
- `monitoring` : prometheus :9090 + grafana :3000 (datasource + dashboard).
- `training` : venv `/opt/ml-env`, copie train/evaluate/preprocess + churn.csv.

### 4.7 Kubernetes (`kubernetes/`)

Deployment `churn-api` (2 replicas, image `churn-api:latest`, probes liveness/readiness),
Service ClusterIP, Ingress nginx, HPA (min 2 max 8 CPU 60 %), StatefulSet Postgres 16
+ PVC 5Gi + pvc.

### 4.8 CI/CD (Jenkins)

`jenkins/Jenkinsfile` : Checkout → Test (`pytest api/ tests/` + `python3 ml/evaluate.py`) →
Train (local) → Build (`docker build -t ...:BUILD_NUMBER`) → Deploy
(`kubectl set image deployment/churn-api` + rollout).

---

## 5. Procédure de test

```bash
# Toute la suite pytest (api + schemas + evaluate + train pipeline)
cd mlops-platform-spec && python -m pytest tests/ -v

# Ou ciblée :
python -m pytest tests/test_api.py        # endpoints /health /predict /history /stats
python -m pytest tests/test_schemas.py    # validation Pydantic (422 sur invalides)
python -m pytest tests/test_evaluate.py   # seuils AUC/F1
python -m pytest tests/test_train_pipeline.py  # train→register→artifact end-to-end
```

- `tests/conftest.py` insère repo root, `api/`, `ml/`, `tests/` dans `sys.path`.
- Le gate CI `ml/evaluate.py` sort en code non nul si AUC < 0.75 ou F1 < 0.30.

**Validation statique / infra** :
```bash
terraform validate -backend=false   # dans terraform/ (provider Docker, pas de remote state)
ansible-playbook --syntax-check site.yml   # dans ansible/
```

---

## 6. Points d'attention (audit du code)

1. **Secrets hardcodés** : `api/db.py` mot de passe par défaut `postgres` ;
   `kubernetes/database/statefulset.yaml` `change-me-in-production` ; IPs placeholder dans
   `Jenkinsfile`/`configmap`. À externaliser en secrets locaux.
2. **DB dans le chemin de requête** : le `/predict` peut écrire en DB (risque 500 si Postgres
   down) ; le `main.py` courant ne l'écrit pas systématiquement.
3. **MI** : les encodeurs sont ré-ajustés par requête ; **M2** : chemins relatifs dans
   `train.py` (dépendant du CWD) ; **M3** : crash roc_auc single-class ; **M4** : double encode
   dans `evaluate.py` ; **M5** : imports absolus cassent `import api.main`.

---

## 7. Références

- [README principale](./README.md) — vue d'ensemble Ferry (ALL-LOCAL).
- [`mlops-platform-spec.md`](./mlops-platform-spec.md) — spec de référence (legacy, à relire
  comme historique de la refonte).
- `tests/QA-REPORT.md` — bugs identifiés en QA.
- `docs/PRD.md` — PRD initial (crédit risk) ; `docs/architecture.md`, `docs/deployment.md`.