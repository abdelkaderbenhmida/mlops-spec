# Enterprise MLOps Platform — Customer Churn Prediction

An end-to-end MLOps platform for a **customer churn prediction** service, provisioned
with infrastructure-as-code across **two cloud providers** and operated with
Kubernetes, Ansible, and Jenkins.

The platform implements the full ML lifecycle — **train → track → serve → monitor** —
across Google Cloud (GCP) and Oracle Cloud (OCI):

- Model training, experiment tracking (MLflow), and monitoring (Prometheus + Grafana) run on OCI.
- The prediction API (FastAPI) runs on a self-managed Kubernetes cluster on GCP.

> Scope is intentionally scoped — no enterprise overengineering. No AWS or Azure,
> no service mesh, no Helm, no Vault. See `mlops-platform-spec.md` for the full spec.

---

## Architecture

```
                          +--------------------------------------------------------------+
                          |                        ORACLE CLOUD (OCI)                      |
                          |                                                              |
  +--------------+        |  +------------------+          +----------------------------+ |
  |  Developers  |        |  |   oci-training   |          |       oci-monitoring       | |
  |  / CI (Jenkins)       |  |  10.0.2.10       |          |       10.0.2.11            | |
  +------+-------+        |  |  MLflow (5000)   |          |  Prometheus (9090)         | |
         |                |  |  PostgreSQL      |          |  Grafana (3000)            | |
         |  ssh / git      |  |  training env    |          |  k6 (load tests)          | |
         |                |  +--------+---------+          +------------+---------------+ |
         |                |           |                               |                  |
         |                +-----------+-------------------------------+------------------+
         |                            | node exporter :9100 (public IP, allowlisted)
         |                            | MLflow :5000 (public IP)
         |                            v
         |                +--------------------------------------------------------------+
         |                |                         GOOGLE CLOUD (GCP)                   |
         |                |                                                              |
         |                |   Kubernetes cluster (self-managed, kubeadm)                 |
         |                |   +--------------+  +--------------+  +--------------+       |
         |                |   | gcp-k8s-cp   |  |  gcp-k8s-w1  |  |  gcp-k8s-w2  |       |
         |                |   | 10.0.1.10    |  |  10.0.1.11   |  |  10.0.1.12   |       |
         |                |   | control-plane |  |  worker      |  |  worker      |       |
         |                |   +------+-------+  +--------------+  +--------------+       |
         |                |          |                                                    |
         |                |          v                                                    |
         |                |   +-----------------------------------+                      |
         |                |   |  K8s namespace "mlops"            |                      |
         |                |   |  churn-api Deployment (FastAPI)   |                      |
         |                |   |  PostgreSQL StatefulSet           |                      |
         |                |   |  (predictions table)              |                      |
         |                |   +-----------------------------------+                      |
         |                |        |  /metrics :80 / :8000 (NodePort/Ingress)           |
         |                +--------+----------------------------------------------------+
         |                         |  Prometheus scrapes GCP node exporters + churn-api
         |                         |  over public IPs (GCP firewall :9100 allows OCI only)
         +-------------------------+
```

**Data flow (serving):** `POST /predict` → FastAPI loads the registered MLflow model
(`churn-model`) from OCI, predicts churn, persists the prediction in PostgreSQL, and
returns `{prediction, probability}`.

**Monitoring flow:** Prometheus on `oci-monitoring` scrapes node exporters on all five VMs
and the API's `/metrics` endpoint; Grafana visualizes node, cluster, and ML API metrics.
k6 load tests run from `oci-monitoring` against the GCP API.

---

## Cloud Split

| Cloud | Role | VMs |
|---|---|---|
| **Google Cloud (GCP)** | Serving — Kubernetes cluster + ML inference API | `gcp-k8s-cp`, `gcp-k8s-w1`, `gcp-k8s-w2` |
| **Oracle Cloud (OCI)** | Training + monitoring — model training, MLflow, Prometheus, Grafana | `oci-training`, `oci-monitoring` |

Networking between clouds relies on **IP allowlisting** over public IPs (no VPN):

- OCI Prometheus scrapes GCP node exporters (`:9100`) and the churn API (`/metrics`).
- GCP firewall restricts port `9100` to the OCI monitoring VM's public IP
  (`node_exporter_source_cidrs` variable).
- MLflow on OCI (`:5000`) is reachable from GCP Kubernetes pods via its public IP.

---

## Stack

| Layer | Tool |
|---|---|
| Infrastructure-as-Code | Terraform (separate state per provider, shared modules) |
| Configuration management | Ansible (role-based, idempotent) |
| Containers | Docker |
| Orchestration | Kubernetes (kubeadm 1.28, self-managed, Calico CNI) |
| CI/CD | Jenkins (Docker container on `gcp-k8s-cp`) |
| Experiment tracking | MLflow 2.10 |
| Model serving | FastAPI + Uvicorn |
| Database | PostgreSQL (MLflow backend store + predictions table) |
| Metrics | Prometheus 2.51 + Grafana 10.3 |
| Load testing | k6 |
| ML framework | scikit-learn (Random Forest) |

---

## Repository Structure

```
mlops-platform-spec/
├── terraform/
│   ├── gcp/                      # GCP provider: VPC, firewall, 3 k8s VMs
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   ├── oracle/                   # OCI provider: VCN, security list, 2 VMs
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   └── modules/
│       ├── network/              # reusable VPC/VCN + firewall/security list
│       └── vm/                   # reusable compute instance (GCP/OCI)
├── ansible/
│   ├── inventory/
│   │   └── hosts.yml             # static fallback inventory
│   ├── playbooks/
│   │   ├── site.yml              # master playbook (all hosts)
│   │   ├── k8s.yml               # Kubernetes cluster (GCP)
│   │   ├── ml.yml                # MLflow + training env (OCI)
│   │   └── monitoring.yml        # Prometheus + Grafana (OCI)
│   └── roles/
│       ├── common/               # base packages, UFW, timezone, node exporter
│       ├── docker/               # Docker CE + daemon config (json-file, 10m)
│       ├── kubernetes/           # kubeadm, kubelet, kubectl, Calico, join
│       ├── mlflow/               # MLflow server + PostgreSQL backend (Docker)
│       ├── monitoring/           # Prometheus + Grafana (Docker, provisioned)
│       └── training/             # Python 3.11 venv, pip deps, training scripts
├── kubernetes/
│   ├── namespace.yaml            # namespace "mlops"
│   └── api/
│       └── deployment.yaml       # churn-api Deployment (2 replicas, probes)
├── docker/
│   └── api/
│       └── Dockerfile            # python:3.11-slim, non-root, port 8000
├── ml/
│   ├── data/
│   │   └── churn.csv             # ~7k synthetic Telco churn rows
│   ├── train.py                  # train RF, log to MLflow, register model
│   ├── evaluate.py               # accuracy gate (>= 0.75, CI)
│   ├── preprocess.py             # shared encoding + split helpers
│   ├── generate_churn_data.py    # regenerate synthetic dataset
│   └── requirements.txt
├── api/
│   ├── main.py                   # FastAPI: /health, /predict, /predictions, /metrics
│   ├── model.py                  # MLflow model loading + prediction
│   ├── schemas.py                # Pydantic request/response models
│   ├── db.py                     # SQLAlchemy + PostgreSQL
│   └── requirements.txt
├── jenkins/
│   └── Jenkinsfile               # CI/CD pipeline (see spec §CI/CD)
├── monitoring/
│   ├── prometheus.yml            # scrape targets (see spec §Monitoring)
│   ├── grafana/
│   │   └── dashboards/
│   └── k6/
│       └── loadtest.js           # k6 load test (see spec §Load Testing)
├── docs/
│   ├── architecture.md           # this project's architecture in depth
│   └── deployment.md             # end-to-end deployment guide
├── mlops-platform-spec.md        # source of truth for the platform design
└── Makefile                      # convenience targets (see Key Commands)
```

> Note: `jenkins/`, `monitoring/`, the remaining `kubernetes/` manifests
> (service, HPA, ingress, ConfigMap, database StatefulSet) and `Makefile` are
> defined by `mlops-platform-spec.md` and land in the `agent/backend` branch.

---

## Deployment Order

Deploy OCI first — the Kubernetes API pods load their model from MLflow at startup.

```
1. terraform apply  (terraform/oracle/)  → OCI VMs up first (MLflow needed before API)
2. terraform apply  (terraform/gcp/)     → GCP VMs created
3. ansible-playbook site.yml             → all servers configured, K8s initialized
4. python ml/train.py                    → model trained, registered in MLflow
5. kubectl apply -f kubernetes/          → API + DB deployed
6. Jenkins configured (manual, first time only)
7. k6 run loadtest.js                    → validate performance + HPA triggers
```

---

## Key Commands

```bash
# 1. Provision infrastructure (run from each provider directory)
cd terraform/oracle && terraform init && terraform apply
cd terraform/gcp    && terraform init && terraform apply

# 2. Configure all servers (inventory generated from Terraform outputs)
ansible-playbook -i inventory/hosts.yml site.yml

# 3. Train + register the churn model (on oci-training, or locally with MLflow reachable)
python ml/train.py

# 4. Deploy the API and database to Kubernetes (from gcp-k8s-cp)
kubectl apply -f kubernetes/

# 5. Load test (run from oci-monitoring)
k6 run loadtest.js
```

See [docs/deployment.md](docs/deployment.md) for the full walkthrough.

---

## Acceptance Criteria

- [ ] `terraform apply` creates all 5 VMs with zero manual steps
- [ ] `ansible-playbook site.yml` configures everything, K8s cluster healthy
- [ ] `kubectl get nodes` shows 3 nodes `Ready`
- [ ] `python ml/train.py` completes and model appears in MLflow UI
- [ ] `POST /predict` returns a valid prediction
- [ ] `GET /predictions` returns records from PostgreSQL
- [ ] HPA scales API pods up under k6 load
- [ ] Grafana shows live node + API + ML metrics
- [ ] Jenkins pipeline runs end-to-end on push to `main`
- [ ] k6 passes p95 < 1000 ms threshold
- [ ] Zero hardcoded credentials anywhere in the repo
