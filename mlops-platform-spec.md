# Enterprise MLOps Platform — Agent Spec

## Goal

Deploy a real ML pipeline (train → track → serve → monitor) across two cloud providers using IaC, Kubernetes, and CI/CD. Scope is intentionally scoped — no enterprise overengineering.

---

## Cloud Split

| Cloud | Role |
|---|---|
| **Google Cloud (GCP)** | Kubernetes cluster + ML inference API |
| **Oracle Cloud (OCI)** | Model training + MLflow + monitoring |

> No AWS or Azure. Add only if explicitly requested.

---

## Stack (fixed — do not substitute)

| Layer | Tool |
|---|---|
| IaC | Terraform |
| Config management | Ansible |
| Containers | Docker |
| Orchestration | Kubernetes (kubeadm, self-managed) |
| CI/CD | Jenkins (Docker container) |
| Experiment tracking | MLflow |
| Model serving | FastAPI |
| Database | PostgreSQL |
| Metrics | Prometheus + Grafana |
| Load testing | k6 |
| ML framework | scikit-learn |

---

## ML Use Case: Customer Churn Prediction

Use the [Telco Customer Churn dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) (public, CSV, ~7k rows).

**Model**: Random Forest classifier (scikit-learn)  
**Target**: `Churn` (binary)  
**Features**: tenure, MonthlyCharges, TotalCharges, Contract, PaymentMethod (encoded)

Keep it simple — the DevOps/MLOps infrastructure is the point, not the model accuracy.

---

## Infrastructure

### GCP VMs

| Name | Role | Size |
|---|---|---|
| `gcp-k8s-cp` | Kubernetes control plane | e2-medium |
| `gcp-k8s-w1` | Kubernetes worker 1 | e2-medium |
| `gcp-k8s-w2` | Kubernetes worker 2 | e2-medium |

> 3 nodes. Do not add a dedicated PostgreSQL VM — run it inside Kubernetes as a StatefulSet.

### OCI VMs

| Name | Role | Shape |
|---|---|---|
| `oci-training` | Model training + MLflow server | VM.Standard.E2.1.Micro |
| `oci-monitoring` | Prometheus + Grafana | VM.Standard.E2.1.Micro |

> Use OCI Always Free tier. No separate load testing VM — run k6 from `oci-monitoring`.

---

## Repository Structure

```
enterprise-mlops-platform/
├── terraform/
│   ├── gcp/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   ├── oracle/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   └── modules/
│       ├── vm/
│       └── network/
├── ansible/
│   ├── inventory/
│   │   └── hosts.yml
│   ├── roles/
│   │   ├── common/          # base packages, UFW, SSH hardening
│   │   ├── docker/          # Docker CE + daemon config
│   │   ├── kubernetes/      # kubeadm, kubelet, kubectl
│   │   ├── mlflow/          # MLflow tracking server (Docker)
│   │   ├── monitoring/      # Prometheus + Grafana (Docker)
│   │   └── training/        # Python 3.11, pip deps, training script
│   └── playbooks/
│       ├── site.yml          # master playbook
│       ├── k8s.yml
│       ├── ml.yml
│       └── monitoring.yml
├── kubernetes/
│   ├── namespace.yaml
│   ├── api/
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   ├── hpa.yaml
│   │   └── ingress.yaml
│   ├── database/
│   │   ├── statefulset.yaml
│   │   ├── pvc.yaml
│   │   └── secret.yaml
│   └── configmap.yaml
├── docker/
│   └── api/
│       └── Dockerfile
├── ml/
│   ├── data/
│   │   └── churn.csv
│   ├── train.py
│   ├── evaluate.py
│   ├── preprocess.py
│   └── requirements.txt
├── api/
│   ├── main.py              # FastAPI app
│   ├── model.py             # load model + predict
│   ├── schemas.py           # Pydantic models
│   ├── db.py                # SQLAlchemy + PostgreSQL
│   └── requirements.txt
├── jenkins/
│   └── Jenkinsfile
├── monitoring/
│   ├── prometheus.yml
│   ├── grafana/
│   │   └── dashboards/
│   └── k6/
│       └── loadtest.js
└── docs/
    ├── architecture.md
    └── deployment.md
```

---

## Terraform Requirements

- Separate state per provider
- Reusable modules in `modules/vm/` and `modules/network/`
- No hardcoded credentials — all via variables
- Outputs: VM public IPs, internal IPs, network IDs

### GCP module creates
- VPC + subnet (`10.0.1.0/24`)
- Firewall: SSH 22, HTTP 80, HTTPS 443, K8s API 6443, node ports 30000–32767, node exporter 9100 (OCI IP only)
- 3 VMs with static internal IPs

### OCI module creates
- VCN + subnet (`10.0.2.0/24`)
- Security list: SSH, MLflow 5000, Prometheus 9090, Grafana 3000
- 2 VMs

---

## Ansible Requirements

- Dynamic inventory populated from Terraform outputs
- All roles idempotent — safe to re-run
- `common` role runs on every host

### Role responsibilities

**common**: apt update, install git/curl/wget/unzip, configure UFW, set UTC timezone

**docker**: install Docker CE, add ubuntu user to docker group, configure daemon (`log-driver: json-file`, `max-size: 10m`)

**kubernetes**: install kubeadm 1.28, kubelet, kubectl; disable swap permanently; init cluster on CP with `--pod-network-cidr=192.168.0.0/16`; install Calico CNI; join workers with token

**mlflow**: run `mlflow server` as Docker container, backend store PostgreSQL (on OCI), artifact store local `/mlflow/artifacts`, expose port 5000

**monitoring**: run Prometheus + Grafana as Docker containers; configure Prometheus scrape targets (see Monitoring section)

**training**: install Python 3.11, pip install from `ml/requirements.txt`, copy training scripts, set `MLFLOW_TRACKING_URI` env var

---

## ML Pipeline

### train.py

```python
# Steps:
# 1. Load churn.csv
# 2. Drop customerID, encode categoricals (LabelEncoder)
# 3. Train/test split 80/20, random_state=42
# 4. Train RandomForestClassifier(n_estimators=100)
# 5. Log to MLflow: params, metrics (accuracy, f1, roc_auc)
# 6. Register model in MLflow Model Registry as "churn-model"
# 7. Save model artifact: model.pkl
```

### evaluate.py

```python
# Load registered model from MLflow
# Run predictions on test set
# Print classification report
# Exit 1 if accuracy < 0.75 (CI gate)
```

### ml/requirements.txt

```
scikit-learn==1.4.0
pandas==2.1.0
mlflow==2.10.0
psycopg2-binary
```

---

## API (FastAPI)

### Endpoints

```
GET  /health          → {"status": "ok", "model_version": "..."}
POST /predict         → {"prediction": 0|1, "probability": 0.87}
GET  /predictions     → list of past predictions from PostgreSQL
```

### /predict request body

```json
{
  "tenure": 12,
  "monthly_charges": 65.5,
  "total_charges": 786.0,
  "contract": "Month-to-month",
  "payment_method": "Electronic check"
}
```

### Implementation notes

- Load model from MLflow on startup using `mlflow.sklearn.load_model()`
- `MLFLOW_TRACKING_URI` injected via K8s ConfigMap
- Store each prediction in PostgreSQL table `predictions(id, input_json, prediction, probability, created_at)`
- Expose `/metrics` endpoint via `prometheus-fastapi-instrumentator`
- Dockerfile: `python:3.11-slim`, non-root user, port 8000

---

## Kubernetes Manifests

All resources in namespace `mlops`.

### API Deployment

```yaml
replicas: 2
resources:
  requests: {cpu: 250m, memory: 256Mi}
  limits:   {cpu: 500m, memory: 512Mi}
```

### HPA (Horizontal Pod Autoscaler)

```yaml
minReplicas: 2
maxReplicas: 8
targetCPUUtilizationPercentage: 60
```

### Database (PostgreSQL StatefulSet)

- 1 replica, PVC 5Gi
- Credentials in K8s Secret
- Init SQL: create `predictions` table

### ConfigMap

```yaml
MLFLOW_TRACKING_URI: http://<oci-training-ip>:5000
DB_HOST: postgres-service
```

---

## CI/CD Pipeline (Jenkinsfile)

```groovy
stages:
  1. Checkout          // git clone
  2. Test              // pytest api/ && python ml/evaluate.py
  3. Train             // ssh to oci-training: python ml/train.py
  4. Build             // docker build -t <registry>/churn-api:$BUILD_NUMBER
  5. Push              // docker push
  6. Deploy            // kubectl set image deployment/churn-api ...
```

- Triggered on push to `main`
- Jenkins runs as Docker container on `gcp-k8s-cp`
- Docker Hub credentials → Jenkins credential store
- Kubeconfig → Jenkins secret file
- OCI SSH key → Jenkins SSH credential
- Pipeline fails if evaluate.py exits 1 (accuracy gate)

---

## Monitoring

### Prometheus scrape targets (`prometheus.yml`)

```yaml
- job_name: node_gcp
  static_configs:
    - targets: ['<gcp-cp-ip>:9100', '<gcp-w1-ip>:9100', '<gcp-w2-ip>:9100']

- job_name: node_oci
  static_configs:
    - targets: ['<oci-training-ip>:9100', '<oci-monitoring-ip>:9100']

- job_name: churn_api
  static_configs:
    - targets: ['<gcp-lb-ip>:80']   # /metrics via ingress
  metrics_path: /metrics
```

Node exporter installed on all VMs via Ansible `common` role.

### Grafana dashboards

| Dashboard | Import ID |
|---|---|
| Node Exporter Full | `1860` |
| Kubernetes cluster | `315` |
| ML API (custom) | — build manually |

Custom ML dashboard panels:
- Total predictions (counter)
- Prediction rate (rate over 5m)
- API p95 latency
- HTTP error rate

---

## Load Testing (k6)

`monitoring/k6/loadtest.js`:

```javascript
// 20 virtual users, 2 minutes
// 70% GET /health, 30% POST /predict
// Thresholds:
//   http_req_duration p(95) < 1000ms
//   http_req_failed < 1%
// Run from oci-monitoring VM
// Target: GCP external IP / ingress
```

---

## Networking Between Clouds

- OCI Prometheus scrapes GCP node exporters over **public IPs**
- GCP firewall allows port 9100 inbound from OCI monitoring IP only
- MLflow on OCI accessible from GCP K8s pods via public IP + port 5000
- No VPN required — IP allowlisting is sufficient for this scope

---

## Deployment Order

```
1. terraform apply (oracle/) → OCI VMs up first (MLflow needed before API)
2. terraform apply (gcp/)    → GCP VMs created
3. ansible-playbook site.yml → all servers configured, K8s initialized
4. python ml/train.py        → model trained, registered in MLflow
5. kubectl apply -f kubernetes/ → API + DB deployed
6. Jenkins configured (manual, first time only)
7. k6 run loadtest.js        → validate performance + HPA triggers
```

---

## What NOT to Build

- No AWS or Azure (out of scope)
- No dedicated Jenkins VM — run as Docker container
- No dedicated PostgreSQL VM — StatefulSet inside K8s
- No Vault or external secrets manager — K8s Secrets is enough
- No Helm — raw manifests only
- No service mesh (Istio, Linkerd)
- No data versioning (DVC) — single CSV file is fine
- No model feature store
- No A/B testing or canary deployment
- No JMeter or Locust — k6 only
- No multi-region setup
- No GPU instances

---

## Acceptance Criteria

- [ ] `terraform apply` creates all 5 VMs with zero manual steps
- [ ] `ansible-playbook site.yml` configures everything, K8s cluster healthy
- [ ] `kubectl get nodes` shows 3 nodes Ready
- [ ] `python ml/train.py` completes and model appears in MLflow UI
- [ ] `POST /predict` returns a valid prediction
- [ ] `GET /predictions` returns records from PostgreSQL
- [ ] HPA scales API pods up under k6 load
- [ ] Grafana shows live node + API + ML metrics
- [ ] Jenkins pipeline runs end-to-end on push to `main`
- [ ] k6 passes p95 < 1000ms threshold
- [ ] Zero hardcoded credentials anywhere in the repo
