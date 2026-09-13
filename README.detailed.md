# Ferry — Plateforme ML Portable Multi-Cloud (README détaillé)

> Documentation complète du code source de **Ferry** (répertoire `mlops-platform-spec`) :
> description, outils, fonctionnement et procédure de test. Complète la
> [README principale](./README.md) et la [spec](./mlops-platform-spec.md).
>
> **⚠️ IMPORTANT — Écart spec / code** : les docs (README, spec, ENTERPRISE-UPGRADE, docs/)
> décrivent le design cible **"Ferry"** (symétrique GCP+OCI, modèle de doléance d'assurance,
> IPsec, exit drills, portability contract, Helm, MLflow sur stockage S3-compatible). Le code
> **implémenté** correspond à un design **asymétrique antérieur** : crédit (German Credit Data)
> + churn API, un seul VM d'entraînement MLflow sur OCI. Les artefacts référencés
> (`helm/lapse-api`, `portability-contract.yaml`, `exit-drills/`, `retention_feedback.py`,
> `terraform/control`, `terraform/ipsec`) sont **absents** — les docs sont aspirationnelles pour
> la montée en version enterprise.

---

## 1. Vue d'ensemble

**Objectif déclaré (Ferry)** : un ML platform **portable entre deux clouds** (GCP + OCI) pour
la prévision de **lapse / renouvellement d'assurance** en finance européenne sous **DORA**.
La justification "pourquoi deux clouds ?" : les entités financières UE doivent prouver leur
capacité à **quitter un fournisseur cloud** (DORA Art. 28 sorties, Art. 29 risque de
concentration) — et la seule preuve crédible est de le faire, en continu, dans la CI.

Le **test de sortie est un job de CI** : basculement de 100 % du trafic vers le fournisseur
survivant en ≤ 4 h (RTO, ≤ 15 min RPO), avec un **Exit Drill Report** signé chaque mois.

### Ce que contient réellement le code

Un pipeline crédit (RandomForest/GradientBoosting sur German Credit Data) servi par FastAPI,
avec : Terraform multi-cloud (modules GCP/OCI), Ansible (roles kubernetes/mlflow/monitoring/
training), Kubernetes (déploiement churn), Prometheus/Grafana, k6, Jenkins, une suite de
tests pytest, et une UI de dashboard.

---

## 2. Stack technique et rôle de chaque outil

| Domaine | Outil | Rôle |
|---|---|---|
| Infrastructure-as-Code | **Terraform** | Modules partagés `network` + `vm` ; implémentations `gcp/` et `oracle/` |
| Config management | **Ansible** | Roles idempotents (common, docker, kubernetes, mlflow, monitoring, training) |
| Conteneurs | **Docker** | Image API multi-stage non-root |
| Orchestration | **Kubernetes** (kubeadm 1.28 self-managed) | Namespace `mlops`, deployment `churn-api`, HPA |
| CI/CD | **Jenkins** | Pipeline : test → train → build → push → deploy |
| Tracking/Registry | **MLflow** (2.10) | Log runs + registry model (churn-model) |
| Serving | **FastAPI + Uvicorn** | `/health`, `/predict`, `/history`, `/stats`, `/model-info` |
| DB | **PostgreSQL** + SQLAlchemy | Table `predictions` (ou SQLite fallback) |
| Metrics | **Prometheus + Grafana** (federated) | node_exporter, dashboards API |
| Load test | **k6** | 20 VUs, 2 min, seuils p95<1000ms + rate<0.01 |
| ML | **scikit-learn** | GradientBoosting (crédit), churn RF |
| Secrets (K8s) | Secret Postgres (⚠️ hardcodé "change-me-in-production") | À remplacer |

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
│       ├── churn.csv, credit.csv, fraud.csv
├── tests/
│   ├── conftest.py             # sys.path bootstrap (repo root, api/, ml/, tests/)
│   ├── _data.py                # données German Credit synthétiques
│   ├── test_api.py             # /health, /predict (200 valid, 422), history/stats
│   ├── test_schemas.py         # validation Pydantic (valide/rejet/invalide/borne)
│   ├── test_evaluate.py        # vérifie seuils AUC/F1
│   ├── test_train_pipeline.py  # train→register→artifact (tmp mlruns)
│   └── QA-REPORT.md            # bugs trouvés lors du QA
├── terraform/
│   ├── modules/ (network/, vm/)  # multi-cloud (count-switch GCP|OCI)
│   ├── gcp/                      # VPC 10.0.1.0/24 + 3 VMs k8s (cp/w1/w2)
│   └── oracle/                   # VCN 10.0.2.0/24 + VMs training/monitoring
├── kubernetes/
│   ├── namespace.yaml, configmap.yaml
│   ├── api/ (deployment, service, ingress, hpa)
│   └── database/ (statefulset, pvc, service, init-configmap)
├── ansible/
│   ├── inventory/hosts.yml
│   ├── playbooks/ (site, ml, k8s, monitoring)
│   └── roles/ (common, docker, kubernetes, mlflow, monitoring, training)
├── monitoring/
│   ├── prometheus.yml, grafana/dashboards/ml-api-dashboard.json, k6/loadtest.js
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
  `get_latest_versions` Production/Staging/None) ; non branché sur `main.py` courant.

### 4.5 Infrastructure (Terraform multi-cloud)

- Module `network` : createur VPC (GCP) ou VCN (OCI) selon `count` (var `cloud`).
- Module `vm` : instance GCP/OCI avec IP interne, clé SSH, script de démarrage optionnel.
- `gcp/` : 3 VMs k8s (cp 10.0.1.10, w1 .11, w2 .12), tags control-plane/worker.
- `oracle/` : 2 VMs (training 10.0.2.10, monitoring 10.0.2.11), security list [22,5000,9090,3000].

### 4.6 Configuration (Ansible)

- `common` : timezone UTC, packages, node_exporter + UFW (ports 22/9100/5000/9090/3000).
- `docker` : Docker CE 26.1.4, cgroupdriver systemd, log max-size 10m.
- `kubernetes` : swap off, kernel modules, kubeadm/kubelet/kubectl 1.28, `kubeadm init
  --pod-network-cidr=192.168.0.0/16`, Calico CNI, join workers, wait Ready.
- `mlflow` : 2 conteneurs (postgres backend-binder 127.0.0.1:5432 + serveur mlflow :5000,
  artifact-root **disque local** `/mlflow/artifacts`).
- `monitoring` : prometheus :9090 + grafana :3000 (datasource + dashboard).
- `training` : venv `/opt/ml-env`, copie train/evaluate/preprocess + churn.csv.

### 4.7 Kubernetes (`kubernetes/`)

Deployment `churn-api` (2 replicas, image `churn-api:latest`, probes liveness/readiness),
Service ClusterIP, Ingress nginx, HPA (min 2 max 8 CPU 60 %), StatefulSet Postgres 16
+ PVC 5Gi + pvc.

### 4.8 CI/CD (Jenkins)

`jenkins/Jenkinsfile` : Checkout → Test (`pytest api/ tests/` + `python3 ml/evaluate.py`) →
Train (ssh oci-training) → Build (`docker build -t ...:BUILD_NUMBER`) → Push → Deploy
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
- `tests/test_api.py` : charge une petite GradientBoosting via `install_trained_model`
  (monkeypatch), teste 200 valide / 422 champs manquants / 422 catégorie inconnue.
- Le gate CI `ml/evaluate.py` sort en code non nul si AUC < 0.75 ou F1 < 0.30.

**Validation statique / infra** :
```bash
terraform validate         # dans terraform/ (init -backend=false)
ansible-playbook --syntax-check site.yml   # dans ansible/
```

---

## 6. Points d'attention (audit du code)

> Extraits de `tests/QA-REPORT.md`, à corriger pour aligner le code sur la spec "Ferry".

1. **Écart spec/code majeur** : le code est crédit/churn asymétrique ; la spec décrit un
   design Ferry symétrique (lapse, IPsec, exit drills, Helm, portability contract) **non
   implémenté**.
2. **Secrets hardcodés** (H1) : `api/db.py` mot de passe défaut `postgres` ;
   `kubernetes/database/statefulset.yaml` `change-me-in-production` ; IPs placeholder dans
   `Jenkinsfile`/`configmap`.
3. **DB dans le chemin de requête** (H2) : le `/predict` référencé dans QA-REPORT écrit en DB
   dans le chemin (risque 500 si Postgres down) ; le `main.py` courant ne l'écrit pas.
4. **Mapping de champs** (H4, corrigé) : l'API snake_case vs CSV PascalCase causait un 500.
5. **MI** : les encodeurs sont ré-ajustés par requête ; **M2** : chemins relatifs dans
   `train.py` (dépendant du CWD) ; **M3** : crash roc_auc single-class ; **M4** : double encode
   dans `evaluate.py` ; **M5** : imports absolus cassent `import api.main`.
6. **Chemin MLflow vs churn** : le role Ansible MLflow tourne sur le VM **training** (pas un
   control plane neutre) et son artifact-root est **disque local**, pas S3-compatible comme
   mandate la spec.

---

## 7. Références

- [README principale](./README.md) — vue d'ensemble Ferry.
- [`mlops-platform-spec.md`](./mlops-platform-spec.md) — spec de référence (843 lignes).
- [`ENTERPRISE-UPGRADE.md`](./ENTERPRISE-UPGRADE.md) — transition vers le design portable.
- `tests/QA-REPORT.md` — bugs identifiés en QA.
- `docs/PRD.md` — PRD initial (crédit risk) ; `docs/architecture.md`, `docs/deployment.md`.
