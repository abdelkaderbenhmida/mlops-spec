# Architecture

> ⚠️ **ALL-LOCAL (disponible aussi en [README](./README.md))** — Ce document décrit
> l'architecture **multi-cloud legacy** (GCP + OCI + DORA) de Ferry. Depuis la refonte,
> **Ferry est 100% local** : aucune dépendance cloud, infrastructure provisionnée sur le
> daemon Docker local via Terraform, inventaire Ansible pointant tout sur `127.0.0.1`,
> monitoring loopback. Ce document est conservé comme référence historique.

> (legacy) This document describes the architecture of **Ferry**, a cloud-portable ML platform for
policy lapse and renewal-risk prediction in European financial services: the components,
their responsibilities, the data and control flows between them, and the cross-cloud
networking model.

Source of truth: [`mlops-platform-spec.md`](../mlops-platform-spec.md). This document
describes the platform as specified; the earliest implementation branches (`agent/backend`,
`agent/docs`) carried the earlier asymmetric single-serving design and the Telco churn use
case — both superseded here.

> **Use case note.** The original project targeted *Telco customer churn*. Ferry replaces
> that with **policy lapse / renewal-risk prediction for a European general insurer** — a
> workload that carries actual money, fits the DORA-regulated buyer profile, and gives the
> model a calculable expected-value objective instead of an AUC ceiling. All references to
> churn below are to the old use case; the platform now scores lapse risk.

---

## 1. Overview

The platform is split across two cloud providers, **symmetrically** — both providers run
the same stack and both serve production traffic:

| Cloud | Role |
|---|---|
| **Google Cloud (GCP)** | Primary serving — self-managed Kubernetes cluster (kubeadm), lapse API, Postgres |
| **Oracle Cloud (OCI)** | Secondary serving — self-managed Kubernetes cluster (kubeadm), lapse API, Postgres |

The symmetry is the point. An asymmetric split (GCP serves, OCI only trains) would mean the
secondary has never proven it can serve — the exit test would fail exactly when it matters.
Traffic is distributed 80/20 (GCP primary, OCI secondary) by global DNS, so the secondary
provider's serving path is exercised every day, not just during drills.

Seven hosts are provisioned:

| Host | Cloud | Static internal IP | Role |
|---|---|---|---|
| `gcp-k8s-cp` | GCP | `10.10.0.10` | Kubernetes control plane (kubeadm init, Calico, helm) |
| `gcp-k8s-w1` | GCP | `10.10.0.11` | Kubernetes worker |
| `gcp-k8s-w2` | GCP | `10.10.0.12` | Kubernetes worker |
| `oci-k8s-cp` | OCI | `10.20.0.10` | Kubernetes control plane (kubeadm init, Calico, helm) |
| `oci-k8s-w1` | OCI | `10.20.0.11` | Kubernetes worker |
| `oci-k8s-w2` | OCI | `10.20.0.12` | Kubernetes worker |
| `control-plane` | neutral | — | MLflow tracking server + registry, Jenkins, S3-compatible artifact storage (reachable from both clusters over IPsec; not in the serving path) |

Non-overlapping CIDRs: GCP `10.10.0.0/16`, OCI `10.20.0.0/16` — required for the
site-to-site IPsec tunnel between the VPC and the VCN.

---

## 2. Portability Contract

The core technical artifact. A machine-checkable definition of what "portable" means
(`portability-contract.yaml` in the repo root):

- **Forbidden dependencies** — managed Kubernetes control planes, provider ML platforms
  (Vertex AI / SageMaker / Azure ML), provider-managed databases, provider serverless,
  provider-specific IAM in application code.
- **Required abstractions** — S3-compatible object storage, OCI Distribution Spec container
  registries, Kubernetes Secrets (not provider secret managers), nginx ingress (not
  provider LB controllers), OIDC identity.
- **Exit objectives** — RTO ≤ 4 hours, RPO ≤ 15 minutes.

A CI job parses Terraform plans and Kubernetes manifests and fails the build on any
forbidden dependency. Portability that is not enforced in CI decays within one sprint.

---

## 3. Layer Responsibilities

### 3.1 Infrastructure layer — Terraform

Separate Terraform state per provider; a **shared module interface** with per-provider
implementations.

- **`terraform/modules/network`** — network plane for a provider:
  - GCP: VPC + subnet `10.10.0.0/16`, firewall rules for SSH (22), K8s API (6443),
    NodePorts (30000–32767), node exporter (9100, restricted), and IPsec
    (UDP 500/4500 from the OCI tunnel peer).
  - OCI: VCN + subnet `10.20.0.0/16`, internet gateway, route table, and a security list
    with ingress for SSH and IPsec (UDP 500/4500 from the GCP tunnel peer); MLflow
    reachable from the control plane only.
- **`terraform/modules/vm`** — compute instance on either provider, static internal IP,
  SSH public key, optional startup script.
- **`terraform/modules/ipsec`** — site-to-site IPsec tunnel configuration. Native on both
  providers; a few dozen lines of Terraform.
- All secrets come from variables — **no hardcoded credentials**.
- Outputs expose internal IPs, network IDs, and subnet CIDRs so Ansible can populate its
  inventory and Prometheus its scrape targets.

### 3.2 Configuration layer — Ansible

Role-based, idempotent configuration. `ansible/playbooks/site.yml` is the master playbook.
The same roles run against both provider groups; **config parity is verified**, not
assumed — a post-run check compares package versions, kubeadm/kubelet versions, and
rendered config files across the two clusters. Divergence fails the drill readiness check.

| Role | Hosts | Responsibility |
|---|---|---|
| `common` | all | UTC timezone, base packages, **node exporter** 1.7.0 systemd unit, UFW deny-inbound default + allow `22, 9100, 5000, 9090, 3000` |
| `docker` | all | Docker CE (GPG + apt repo), daemon config (`json-file`, `max-size: 10m`), `ubuntu` in docker group |
| `kubernetes` | both k8s groups | swap off, kernel modules + sysctl, kubeadm/kubelet/kubectl **1.28** (held), containerd systemd cgroup driver, `kubeadm init --pod-network-cidr=192.168.0.0/16`, Calico CNI v3.27.2, kubeconfig for `ubuntu`, worker join, wait for all nodes `Ready` — **identical roles, identical versions, both providers** |
| `mlflow` | `control-plane` | `mlflow-db` (postgres:16, backend store) + `mlflow` containers; `mlflow server --host 0.0.0.0 --port 5000 --backend-store-uri postgresql://… --default-artifact-root s3://…` — **artifact store on S3-compatible object storage**, never local disk, never provider-proprietary artifact APIs |
| `monitoring` | per-provider hosts | **local** Prometheus scraping only its own cluster; central Grafana federates aggregated series from both (see §4.4) |
| `training` | `control-plane` | Python 3.11 + venv `/opt/ml-env`, `pip install -r /opt/ml/requirements.txt`, copy training scripts + policy data to `/opt/ml`, set `MLFLOW_TRACKING_URI` |

### 3.3 ML pipeline layer — `ml/`

| File | Responsibility |
|---|---|
| `train.py` | Load the ~400k-row policy book (date-partitioned), engineer features (tenure, premium, product line, price sensitivity, seasonality, prior claims), train a gradient-boosting classifier on the lapse target, **rank by `P(lapse) × premium × P(save | contacted)` and take the top N within retention capacity**, log params/metrics (expected value at budget, precision@N, f1, roc_auc) to MLflow, register **`lapse-model`** in the Model Registry |
| `evaluate.py` | Load the latest `lapse-model`, compute hold-out expected value at the fixed intervention budget, print the report (EV, precision@N, contact cost vs. retained premium), **exit 1 if EV is below the gate** (CI gate on expected value, not AUC) |
| `preprocess.py` | Shared feature encoding + date-partitioned split so train and evaluate encodings match |
| `retention_feedback.py` | Ingest retention campaign outcomes (contacted → renewed/lapsed), join to scored policies, publish as labels within 60 days of scoring — the feedback loop that keeps the model economically honest |

**The model objective.** The earlier churn spec optimized AUC; that produced a model nobody
could price. Ferry optimizes **expected value at a fixed intervention budget**: the model's
value is calculable (€582k retained premium on ~€40k of intervention cost per year at
2 percentage points of saved lapsing book), and precision matters because intervention cost
scales with how many policies you contact.

### 3.4 Serving layer — FastAPI (`api/`)

| File | Responsibility |
|---|---|
| `main.py` | FastAPI app: `GET /health`, `POST /score`, `GET /predictions`, `GET /metrics` (via `prometheus-fastapi-instrumentator`); initializes DB tables and loads the MLflow model on startup; `/health` reports the `cluster` field so traffic-split verification can confirm both providers serve |
| `model.py` | Loads the registered `lapse-model` from MLflow (`models:/lapse-model/<version>`), applies the training encoders, returns `(probability, expected_value, bucket)` |
| `schemas.py` | Pydantic models: `ScoreRequest`, `ScoreResponse`, `HealthResponse`, `PredictionRecord` |
| `db.py` | SQLAlchemy `scores` table (`id, policy_id, input_json, probability, expected_value, bucket, created_at`); DB URL from env vars |

`docker/api/Dockerfile` builds the API image on `python:3.11-slim` as non-root user
`appuser` (uid 1000), exposing port 8000.

### 3.5 Orchestration layer — Kubernetes + Helm

Both clusters run namespace `mlops`, deployed from the **same Helm chart**
(`helm/lapse-api`) with per-provider values files (`values-gcp.yaml`, `values-oci.yaml`):

- API Deployment: 2 replicas; requests `cpu: 250m, memory: 256Mi`; limits
  `cpu: 500m, memory: 512Mi`; liveness/readiness on `/health`.
- HPA: `minReplicas: 2, maxReplicas: 8`, `targetCPUUtilizationPercentage: 60`.
- PostgreSQL StatefulSet: 1 replica, PVC 5Gi, init SQL for `scores`.
- Ingress: **nginx ingress** (per the Portability Contract — never provider LB
  controllers), serving both `:80` traffic and `/metrics`.
- Secrets: **Sealed Secrets** with keys held outside both clouds — Kubernetes Secrets are
  base64, not encryption, and provider KMS violates the contract.
- mTLS: cert-manager-issued certificates between services.

Helm is included deliberately: two environments with per-provider differences is exactly
what values files solve. Raw manifests mean copy-paste divergence — the failure mode this
platform exists to prevent.

### 3.6 CI/CD — Jenkins

Jenkins runs as a Docker container on the neutral control plane, triggered on push to
`main`:

1. Checkout → 2. **Portability check** (parse plans + manifests against the contract; fail
   on forbidden dependency) → 3. Test (`pytest api/` + `python ml/evaluate.py` EV gate) →
   4. Train (`python ml/train.py`, control plane) → 5. Build → 6. Push → 7. Deploy
   (Helm, `values-gcp.yaml`) → 8. Deploy (Helm, `values-oci.yaml`) → 9. Post-deploy check
   (`/health` on both clusters, model version match).

The pipeline fails if `evaluate.py` exits 1 or the portability check trips. Credentials are
held in the Jenkins credential store.

### 3.7 The Exit Drill

The signature capability: a scheduled, automated, evidence-producing failover, run
monthly in business hours:

```
T+0     Freeze deploys. Snapshot state. Announce drill start.
T+2m    Shift DNS: GCP 80/20 → 0/100 OCI.
T+5m    Verify: p95 latency, error rate, prediction volume, model version served.
T+10m   Run the full k6 suite against OCI only. HPA must scale.
T+20m   Verify MLflow registry reachable, model reload works, training job can start.
T+30m   Scoring-parity test: 10,000 stored feature vectors scored on both providers
        must produce identical predictions to floating-point tolerance.
T+45m   Restore 80/20. Confirm recovery.
T+50m   Generate signed Exit Drill Report.
```

The T+30m parity test makes the drill credible rather than theatrical: failover that
serves traffic but produces different predictions (library version skew, base-image
drift, stale model on the secondary) is a silent correctness failure worse than an
outage. Each drill produces a signed evidence bundle under `exit-drills/<date>/` —
`summary.json` (RTO/RPO achieved, pass/fail per objective), `traffic_timeline.png`,
`latency_comparison.md`, `parity_report.json`, `failures.md` (remediation owner + due
date), and `manifest.json` (SHA-256 of every file). Twelve of these per year is what the
institution hands the regulator.

---

## 4. Data, Control, and Monitoring Flow

### 4.1 Training flow (control plane)

```
control-plane
  python ml/train.py
        │  mlflow.set_tracking_uri(http://control-plane:5000)
        ▼
  MLflow Tracking Server (Docker, :5000)
        ├─ backend store → PostgreSQL (mlflow-db, 127.0.0.1:5432)
        └─ artifact store → S3-compatible object storage
        │
        ▼
  Model Registry: "lapse-model" (registered, version N)
```

- `ml/train.py` trains the gradient booster on the ~400k-row policy book, ranks by
  expected value under the retention capacity constraint, logs metrics (EV at budget,
  precision@N, f1, roc_auc), registers `lapse-model`, saves the artifact.
- `ml/evaluate.py` loads the latest registered model and gates CI on the EV threshold.
- `retention_feedback.py` closes the loop: campaign outcomes become labels within 60 days.

### 4.2 Serving flow (data plane) — identical on both providers

```
client ──80/20 DNS──► lapse-api (k8s "mlops", 2 replicas)     GCP (80%) / OCI (20%)
                         │
                         ├─ load model: models:/lapse-model/<version>
                         │      from http://control-plane:5000 (MLflow, over IPsec)
                         ├─ apply encoders, predict P(lapse), compute expected value
                         │
                         ├─ INSERT INTO scores (...) → PostgreSQL StatefulSet (local)
                         │
                         └─ { "probability": 0.31, "expected_value": 41.2, "bucket": "medium" }
```

- `GET /health` → `{"status": "ok", "model_version": "<version>", "cluster": "gcp|oci"}`.
- `GET /predictions?limit=100` → last scores from local PostgreSQL.
- Every score is persisted locally; PostgreSQL also stores the raw input JSON, feeding
  `GET /predictions` and the prediction metrics.

### 4.3 Monitoring flow — federation, not cross-cloud scraping

```
GCP (local Prometheus :9090)           OCI (local Prometheus :9090)
   ├─ scrape :9100 node exporters         ├─ scrape :9100 node exporters
   └─ scrape :80/metrics lapse-api        └─ scrape :80/metrics lapse-api
        │                                       │
        └──────────────┬────────────────────────┘
                       │  /federate over IPsec (aggregated series only, 60s)
                       ▼
              control-plane (central Grafana :3000)
                 └─ dashboards: Node Exporter Full / K8s cluster / ML API / Drill
```

Each provider's Prometheus scrapes **only its own** cluster — no cross-cloud raw
scraping. A central Grafana federates aggregated series. This cuts cross-cloud traffic by
roughly an order of magnitude, removes the tight coupling where a network blip on one side
blanks the other side's dashboards, and keeps egress cost off the bill.

### 4.4 CI/CD flow

```
push to main ──► Jenkins (Docker on control-plane)
   checkout → portability check → test (pytest + EV gate) → train (control-plane)
   → docker build/push lapse-api:$BUILD_NUMBER
   → helm upgrade values-gcp → helm upgrade values-oci → post-deploy health check
```

---

## 5. Networking Between Clouds

The earlier design scraped and served across public IPs with allowlisting only ("no VPN
required"). That is gone: metrics traversing the public internet authenticated by source IP
does not survive a financial-institution security review.

| Flow | Path | Secured by |
|---|---|---|
| API pods → MLflow (control plane) | IPsec tunnel | IPsec + mTLS |
| Central Grafana → provider Promethei | IPsec tunnel (`/federate`) | IPsec |
| Provider Prometheus → local targets | local VPC | VPC-internal |
| Postgres | in-cluster only | cluster network policy + mTLS |
| SSH / admin | operators → all VMs `:22` | UFW + cloud firewall allowlists, SSH keys |
| Kubernetes API | operators / kubeconfig → `:6443` | cloud firewall allowlist |
| k6 load tests | run per provider against its ingress | health-checked endpoints |

- **Site-to-site IPsec** between the GCP VPC (`10.10.0.0/16`) and OCI VCN
  (`10.20.0.0/16`), both providers' native VPN offerings; **no service is reachable by
  public IP allowlist alone**.
- **mTLS between services** (cert-manager) so a compromised network position is still not
  sufficient access.
- **Prometheus federation** instead of cross-cloud scraping, per §4.3.

### Firewall hardening notes

- UFW on each VM (`common` role) is defense-in-depth on top of the cloud firewalls; it
  allows `22, 9100, 5000, 9090, 3000` on the local interface — cross-cloud ports (MLflow,
  federation) are tunnel-only.
- MLflow's PostgreSQL backend store is bound to `127.0.0.1:5432` on the control plane.
- No credentials are baked into the infrastructure: GCP/OCI API credentials, SSH keys,
  and DB/MLflow passwords all flow in through variables, env, and Sealed Secrets.

### Static IP plan

| Subnet | CIDR | Hosts |
|---|---|---|
| GCP (`gcp-subnet`) | `10.10.0.0/16` | `.10` CP, `.11` w1, `.12` w2 |
| OCI (`oci-subnet`) | `10.20.0.0/16` | `.10` CP, `.11` w1, `.12` w2 |

---

## 6. Cost and Risk Profile

Multi-cloud is not free, and Ferry says so in the spec: **~2.2× infrastructure cost
(+€415/mo over single-cloud) and 1.3× operational load**, plus honest risks — the
portability ceiling (K8s/containers/Terraform port well; managed DB features, IAM
semantics, and storage performance do not), operational complexity as the real failure
mode (mitigated by the 80/20 live-traffic split — a rotting secondary serving real
customers is noticed within hours), and the requirement that drills be allowed to fail.
The framing for a buyer: **insurance with a measurable premium**, justified by DORA
exit-evidence requirements and contract-renewal negotiating leverage.
