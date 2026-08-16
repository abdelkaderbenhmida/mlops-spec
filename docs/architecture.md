# Architecture

This document describes the architecture of the Enterprise MLOps Platform for
customer churn prediction: the components, their responsibilities, the data and
control flows between them, and the cross-cloud networking model.

Source of truth: [`mlops-platform-spec.md`](../mlops-platform-spec.md). This
document describes the platform as implemented across the `agent/backend` and
`agent/docs` branches.

---

## 1. Overview

The platform is split across two cloud providers:

| Cloud | Role |
|---|---|
| **Google Cloud (GCP)** | Serving — self-managed Kubernetes cluster (kubeadm) running the churn prediction API |
| **Oracle Cloud (OCI)** | Training + monitoring — MLflow tracking server, training environment, Prometheus, Grafana |

Five VMs are provisioned:

| VM | Cloud | Static internal IP | Role |
|---|---|---|---|
| `gcp-k8s-cp` | GCP | `10.0.1.10` | Kubernetes control plane (kubeadm init, Calico, Jenkins host) |
| `gcp-k8s-w1` | GCP | `10.0.1.11` | Kubernetes worker |
| `gcp-k8s-w2` | GCP | `10.0.1.12` | Kubernetes worker |
| `oci-training` | OCI | `10.0.2.10` | Model training + MLflow server (PostgreSQL backend store) |
| `oci-monitoring` | OCI | `10.0.2.11` | Prometheus + Grafana + k6 load testing |

---

## 2. Layer Responsibilities

### 2.1 Infrastructure layer — Terraform

Separate Terraform state per provider; reusable modules shared between them.

- **`terraform/modules/network`** — creates the network plane for a provider:
  - GCP: VPC + subnet `10.0.1.0/24`, firewall rules for SSH (22), HTTP (80),
    HTTPS (443), K8s API (6443), NodePorts (30000–32767), and node exporter
    (9100, restricted to `node_exporter_source_cidrs`).
  - OCI: VCN + subnet `10.0.2.0/24`, internet gateway, route table, and a
    security list with ingress for `22, 5000, 9090, 3000` (SSH, MLflow,
    Prometheus, Grafana).
- **`terraform/modules/vm`** — creates a compute instance on either provider:
  - GCP: `google_compute_instance` from the `ubuntu-os-cloud`/`ubuntu-2204-lts`
    image family, static internal IP, `access_config {}` for a public IP, SSH
    public key for the `ubuntu` user, optional startup script.
  - OCI: `oci_core_instance` (`VM.Standard.E2.1.Micro`), auto-detected
    availability domain, latest Canonical Ubuntu 22.04 image, static private IP,
    public IP via `assign_public_ip = true`.
- All secrets (GCP service-account JSON path, OCI API-key path, SSH keys) come
  from variables — **no hardcoded credentials**.
- Outputs expose VM public/internal IPs, network IDs, and subnet CIDRs so
  Ansible can populate its inventory and Prometheus its scrape targets.

### 2.2 Configuration layer — Ansible

Role-based, idempotent configuration. `ansible/playbooks/site.yml` is the master
playbook; `k8s.yml`, `ml.yml`, and `monitoring.yml` target subsets.

| Role | Hosts | Responsibility |
|---|---|---|
| `common` | all | UTC timezone, `apt update`, base packages (git, curl, wget, unzip, ca-certificates, gnupg, software-properties-common), **node exporter** 1.7.0 systemd unit, UFW deny-inbound default + allow `22, 9100, 5000, 9090, 3000` |
| `docker` | all | Docker CE (GPG + apt repo), daemon config (`json-file` log driver, `max-size: 10m`, `native.cgroupdriver=systemd`), `ubuntu` in docker group |
| `kubernetes` | `gcp_k8s` | swap off, kernel modules + sysctl, kubeadm/kubelet/kubectl **1.28** (held), containerd systemd cgroup driver, `kubeadm init --pod-network-cidr=192.168.0.0/16`, Calico CNI v3.27.2, kubeconfig for `ubuntu`, worker join via `kubeadm token create --print-join-command`, wait for all nodes `Ready` |
| `mlflow` | `oci-training` | `mlflow-db` (postgres:16, backend store, port 5432 bound to 127.0.0.1) + `mlflow` containers; `mlflow server --host 0.0.0.0 --port 5000 --backend-store-uri postgresql://… --default-artifact-root /mlflow/artifacts`; health-checked on `:5000/health` |
| `monitoring` | `oci-monitoring` | Prometheus 2.51 + Grafana 10.3 containers; Prometheus scrape config rendered from `prometheus_scrape_targets` (from Terraform outputs); Grafana provisioned with the Prometheus datasource, file-based dashboard provider, and the custom **ML API** dashboard |
| `training` | `oci-training` | Python 3.11 + venv `/opt/ml-env`, `pip install -r /opt/ml/requirements.txt`, copy training scripts + `churn.csv` to `/opt/ml`, set `MLFLOW_TRACKING_URI` in `/etc/environment` and `/home/ubuntu/.bashrc` |

### 2.3 ML pipeline layer — `ml/`

| File | Responsibility |
|---|---|
| `generate_churn_data.py` | Regenerate the synthetic ~7k-row Telco churn dataset (`ml/data/churn.csv`) |
| `preprocess.py` | Shared feature encoding (LabelEncoder on `Contract`, `PaymentMethod`) + stratified 80/20 split (`random_state=42`); used by both train and evaluate so encodings match |
| `train.py` | Train `RandomForestClassifier(n_estimators=100, random_state=42)`; log params/metrics (accuracy, f1, roc_auc) to MLflow; register the model as **`churn-model`** in the Model Registry; save `ml/model.pkl` |
| `evaluate.py` | Load the latest `churn-model` from MLflow, run the hold-out test set, print a classification report, **exit 1 if accuracy < 0.75** (CI gate) |

### 2.4 Serving layer — FastAPI (`api/`)

| File | Responsibility |
|---|---|
| `main.py` | FastAPI app: `GET /health`, `POST /predict`, `GET /predictions` (recent predictions from PostgreSQL), `GET /metrics` (via `prometheus-fastapi-instrumentator`); initializes DB tables and loads the MLflow model on startup |
| `model.py` | Loads the registered `churn-model` from MLflow (`models:/churn-model/<version>`), applies the training encoders to request data, returns `(prediction, probability)` |
| `schemas.py` | Pydantic models: `PredictRequest`, `PredictResponse`, `HealthResponse`, `PredictionRecord` |
| `db.py` | SQLAlchemy `predictions` table (`id, input_json, prediction, probability, created_at`); DB URL built from `DB_HOST/DB_PORT/DB_USER/DB_PASSWORD/DB_NAME` env vars |

`docker/api/Dockerfile` builds the API image on `python:3.11-slim` as non-root
user `appuser` (uid 1000), exposing port 8000.

### 2.5 Orchestration layer — Kubernetes

`kubernetes/namespace.yaml` creates namespace `mlops`. `kubernetes/api/deployment.yaml`
deploys `churn-api`:

- 2 replicas; resource requests `cpu: 250m, memory: 256Mi`, limits `cpu: 500m, memory: 512Mi`.
- Config: `MLFLOW_TRACKING_URI` + `DB_HOST` from ConfigMap `mlops-config`;
  `DB_USER`/`DB_PASSWORD` from Secret `postgres-secret`.
- Liveness/readiness probes on `/health`.
- Per the spec: a Service + Ingress (for `:80`), an HPA
  (`minReplicas: 2, maxReplicas: 8, targetCPUUtilizationPercentage: 60`), and a
  PostgreSQL StatefulSet (1 replica, 5Gi PVC, init SQL for `predictions`) land
  in `kubernetes/` alongside these manifests.

### 2.6 CI/CD — Jenkins

Per the spec, Jenkins runs as a Docker container on `gcp-k8s-cp` and is triggered
on push to `main`:

1. Checkout → 2. Test (`pytest api/` + `python ml/evaluate.py`) → 3. Train (ssh to
`oci-training`, `python ml/train.py`) → 4. Build (`docker build` `churn-api:$BUILD_NUMBER`)
→ 5. Push (Docker Hub) → 6. Deploy (`kubectl set image deployment/churn-api …`).

The pipeline fails if `evaluate.py` exits 1 (accuracy gate). Credentials are held
in the Jenkins credential store; the kubeconfig is a Jenkins secret file; the OCI
SSH key is a Jenkins SSH credential.

### 2.7 Monitoring layer — Prometheus + Grafana

Runs on `oci-monitoring` as Docker containers.

- **Prometheus** (port 9090) scrapes, over **public IPs**:
  - `node_gcp`: `:9100` on all three GCP VMs,
  - `node_oci`: `:9100` on both OCI VMs,
  - `churn_api`: the GCP ingress/load-balancer `:80` with `metrics_path: /metrics`.
- **Grafana** (port 3000, admin credentials via role defaults): provisioning adds
  the Prometheus datasource and the file-based dashboard provider. Dashboards:
  Node Exporter Full (1860), Kubernetes cluster (315), and the custom **ML API**
  dashboard whose panels are:

| Panel | Query |
|---|---|
| Total predictions | `sum(http_requests_total{path="/predict"})` |
| Prediction rate (5m) | `sum(rate(http_requests_total{path="/predict"}[5m]))` |
| API p95 latency | `histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))` |
| HTTP error rate | `sum(rate(http_requests_total{status=~"5.."}[5m])) / clamp_min(sum(rate(http_requests_total[5m])), 0.0001)` |

Node exporter is installed on every VM by the `common` Ansible role and runs
`--collector.systemd --collector.processes`.

### 2.8 Load testing — k6

`monitoring/k6/loadtest.js` (per spec): 20 virtual users for 2 minutes, 70% `GET
/health` / 30% `POST /predict`, thresholds `http_req_duration p(95) < 1000ms`
and `http_req_failed < 1%`. Run from `oci-monitoring` against the GCP external
IP / ingress.

---

## 3. Data and Control Flow

### 3.1 Training flow (control plane)

```
oci-training
  python ml/train.py
        │  mlflow.set_tracking_uri(http://<oci-training-ip>:5000)
        ▼
  MLflow Tracking Server (Docker, :5000)
        ├─ backend store → PostgreSQL (mlflow-db, 127.0.0.1:5432)
        └─ artifact store → /mlflow/artifacts
        │
        ▼
  Model Registry: "churn-model" (registered, version N)
```

- `ml/train.py` reads `ml/data/churn.csv`, encodes features, splits 80/20,
  trains the Random Forest, logs params + metrics, registers `churn-model`, and
  saves `ml/model.pkl`.
- `ml/evaluate.py` loads the latest registered model and gates CI on
  `accuracy >= 0.75`.

### 3.2 Serving flow (data plane)

```
client ──POST /predict──► churn-api (K8s, namespace "mlops", 2 replicas)
                             │
                             ├─ load model: models:/churn-model/<version>
                             │      from http://<oci-training-ip>:5000 (MLflow)
                             ├─ apply LabelEncoders (from training data)
                             ├─ RandomForestClassifier.predict / predict_proba
                             │
                             ├─ INSERT INTO predictions (input_json, prediction,
                             │      probability, created_at)  → PostgreSQL StatefulSet
                             │
                             └─ { "prediction": 0|1, "probability": 0.87 }
```

- `GET /health` → `{"status": "ok", "model_version": "<version>"}`.
- `GET /predictions?limit=100` → last predictions from PostgreSQL, newest first.
- Every prediction is persisted; PostgreSQL stores the raw input JSON plus the
  outcome, feeding both `GET /predictions` and the prediction metrics.

### 3.3 Monitoring flow

```
oci-monitoring
  Prometheus (:9090)
     ├─ scrape :9100  (node_gcp — 3 GCP VMs, public IP)
     ├─ scrape :9100  (node_oci — 2 OCI VMs, public IP)
     ├─ scrape :80/metrics (churn_api — GCP ingress, prometheus-fastapi-instrumentator)
     ▼
  Grafana (:3000)  ──► dashboards: Node Exporter Full / K8s cluster / ML API
```

### 3.4 CI/CD flow

```
push to main ──► Jenkins (Docker on gcp-k8s-cp)
   checkout → test (pytest + evaluate.py gate) → train (ssh oci-training)
   → docker build/push churn-api:$BUILD_NUMBER → kubectl set image deployment/churn-api
```

---

## 4. Networking Between Clouds

There is **no VPN or private peering** — connectivity is over public IPs with
**IP allowlisting** at the cloud-firewall layer. This is intentional for scope.

| Flow | Source | Destination | Allowed by |
|---|---|---|---|
| Prometheus → node exporters | `oci-monitoring` (public IP) | `gcp-*:9100` | GCP firewall `gcp-allow-node-exporter`, `source_ranges = node_exporter_source_cidrs` (set to the OCI monitoring VM's `/32` public IP) |
| API pods → MLflow | GCP K8s pods | `oci-training:5000` | OCI security list ingress rule for port 5000 (`oci_security_list_ports = [22, 5000, 9090, 3000]`) |
| Prometheus → API metrics | `oci-monitoring` | GCP ingress `:80/metrics` | GCP firewall `gcp-allow-http` (port 80) |
| SSH / admin | operators | all VMs `:22` | GCP `gcp-allow-ssh` + OCI security list |
| Kubernetes API | operators / kubeconfig | `gcp-k8s-cp:6443` | GCP firewall `gcp-allow-k8s-api` |
| NodePorts (optional) | clients | GCP VMs `30000–32767` | GCP firewall `gcp-allow-nodeports` |

### Firewall hardening notes

- The GCP node-exporter rule is the only one designed to be restricted: set
  `node_exporter_source_cidrs` in `terraform/gcp` to the **public IP of
  `oci-monitoring`** (e.g. `["129.0.0.11/32"]`). The default is `0.0.0.0/0` so
  `terraform apply` completes with zero manual steps — tighten it before
  exposing the cluster to the internet.
- UFW on each VM (`common` role) is defense-in-depth on top of the cloud
  firewalls; it allows `22, 9100, 5000, 9090, 3000`.
- MLflow's PostgreSQL backend store is bound to `127.0.0.1:5432` and is **not**
  exposed publicly; only the MLflow server (`:5000`) is reachable.
- No credentials are baked into the infrastructure: GCP/OCI API credentials,
  SSH keys, and DB/MLflow passwords all flow in through variables, env, and
  Kubernetes Secrets.

### Static IP plan

| Subnet | CIDR | Hosts |
|---|---|---|
| GCP (`gcp-subnet`) | `10.0.1.0/24` | `.10` CP, `.11` w1, `.12` w2 |
| OCI (`oci-subnet`) | `10.0.2.0/24` | `.10` training, `.11` monitoring |
