# Ferry — Local MLOps Platform

> **Ferry** is a complete, all-local MLOps platform: data → model → train → track →
> serve → monitor, running end-to-end on a single local machine (or a handful of local
> VMs). No cloud, no external credentials, no SaaS dependencies.

![Python](https://img.shields.io/badge/Python-3.11%7C3.12-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Stack](https://img.shields.io/badge/stack-All%20Local-brightgreen.svg)
![MLOps](https://img.shields.io/badge/MLOps-MLflow%20%2B%20K8s%20%2B%20Prometheus-blueviolet.svg)

Build a real ML pipeline (train → track → serve → monitor) that runs **entirely on local
infrastructure** you control. Ferry demonstrates the full MLOps lifecycle without any
cloud dependency — the portability story is inverted: nothing can leave the machine because
there is nothing to leave it with.

**The single testable promise of Ferry**:

> Everything — orchestration, tracking, serving, monitoring, CI/CD — runs on local
> infrastructure. There are no cloud accounts, no managed services, and no provider-proprietary
> APIs anywhere in the stack.

## Why All-Local: The Problem

Most MLOps portfolios either assume a cloud account (and never show you the invoices) or stop
short of a real serving + monitoring loop. Ferry removes the cloud entirely, which forces
every component to be self-hosted and provider-neutral:

- **Orchestration** → self-managed Kubernetes (kubeadm)
- **Tracking** → self-hosted MLflow
- **Object storage** → MinIO (S3 API)
- **CI/CD** → self-hosted Jenkins
- **Monitoring** → Prometheus + Grafana
- **Config** → Ansible (local connection)

This is the same stack an air-gapped or on-premises team would run — a genuinely useful
capability, not a cloud demo.

## Stack Components (ALL-LOCAL)

### 1. Terraform — Local Infrastructure as Code
- **What**: IaC for the local stack using the Docker provider
- **How**: `terraform/local` provisions the local Docker network, volumes, Postgres, and
  the MLflow tracking server on the host daemon. No cloud provider, no credentials, no
  remote state.
- **Key files**: `terraform/main.tf`, `terraform/variables.tf`, `terraform/outputs.tf`
- **Usage**: `terraform init && terraform apply`
- **Justification**: Even a local stack deserves reproducible provisioning; Terraform over
  the Docker provider is the IaC answer without a cloud account.

### 2. Ansible — Configuration Management (Local)
- **What**: Provider-neutral config; roles run on the local machine
- **How**: Static inventory maps every logical host to `127.0.0.1` with
  `ansible_connection: local`; roles (`common`, `docker`, `kubernetes`, `mlflow`,
  `monitoring`, `training`) are idempotent
- **Key files**: `ansible/roles/`, `ansible/inventory/hosts.yml`, `ansible/playbooks/`
- **Usage**: `ansible-playbook -i inventory/hosts.yml site.yml`
- **Justification**: Self-hosted CM that needs no managed nodes; the same playbook is
  portable to any set of local VMs.

### 3. Kubernetes (kubeadm) — Self-Managed Orchestration
- **What**: Self-managed K8s (not a managed control plane)
- **How**: kubeadm, kubelet, kubectl; Calico CNI
- **Key files**: `kubernetes/`
- **Usage**: `kubectl get nodes`
- **Justification**: The only way to run orchestration identically everywhere is to manage
  it yourself; a managed control plane is provider-specific by definition.

### 4. MinIO — S3-Compatible Object Storage
- **What**: Local S3-compatible artifact storage
- **How**: MinIO exposes the S3 API; MLflow artifact store and any object needs use it
  rather than local disk or provider storage
- **Key files**: `docker/`, MLflow configuration
- **Usage**: MLflow artifact store

### 5. CI/CD — Jenkins (Self-Hosted)
- **What**: Docker container on the local host
- **How**: Pipeline on push to `main`: checkout → test → train → build → push local image
  → deploy → post-deploy check
- **Key files**: `jenkins/Jenkinsfile`
- **Usage**: Triggered on push to `main`
- **Justification**: CI that runs anywhere — including on pure-local hosts with no internet
  requirement.

### 6. k6 — Load Testing
- **What**: Load testing against the local serving API
- **How**: `monitoring/k6/loadtest.js` runs against `http://localhost:8000`; 20 virtual
  users, 2 minutes; 70% GET /health, 30% POST /score; thresholds p(95) < 1000ms,
  http_req_failed < 1%
- **Key files**: `monitoring/k6/loadtest.js`

### 7. Prometheus + Grafana — Local Monitoring
- **What**: Prometheus scrapes local nodes (node_exporter `localhost:9100`), MLflow
  (`localhost:5000`), and the API (`localhost:8000`); Grafana visualizes
- **How**: All scrape targets are loopback; no cloud IPs
- **Key files**: `monitoring/prometheus.yml`, `monitoring/`

## Docker Compose — Local Stack

`docker/compose.local.yml` runs the core local stack:

```bash
docker compose -f docker/compose.local.yml up -d postgres mlflow
docker compose -f docker/compose.local.yml --profile train run --rm train
docker compose -f docker/compose.local.yml --profile serve up -d api
```

Host ports are configurable via `POSTGRES_HOST_PORT`, `MLFLOW_HOST_PORT`, `API_HOST_PORT`.

## Repository Structure

```
ferry/
├ terraform/         # ALL-LOCAL: Docker-provider IaC (network, volumes, Postgres, MLflow)
├ ansible/           # local-connection inventory + idempotent roles
├ kubernetes/        # kubeadm, cert-manager, nginx-ingress, sealed-secrets bootstrap
├ helm/              # lapse-api chart + values
├ docker/            # compose.local.yml, api/Dockerfile, mlflow/, training/
├ ml/                # data, train.py, evaluate.py, preprocess.py
├ api/               # main.py, model.py, schemas.py, db.py
├ jenkins/           # Jenkinsfile (all-local pipeline)
├ monitoring/        # prometheus.yml, grafana, dashboards, k6/loadtest.js
└ docs/              # architecture.md, deployment.md
```

## ML Use Case: Policy Lapse & Renewal-Risk Prediction

**Use case**: policy lapse and renewal-risk prediction for a European general insurer.

**The business loop**:

```
Policy approaching renewal (T-45 days)
        │
        ▼
Lapse-risk model scores the policy
        │
        ├─ Low risk    → standard renewal notice, no intervention
        ├─ Medium risk → retention email, loyalty discount offer
        └─ High risk   → outbound call from retention team + priced retention offer
```

**Economics**:

- Book size: 400,000 active policies
- Average annual premium: €520
- Baseline annual lapse rate: 14% (~56,000 lapsing policies)
- Retention offer cost: €35 average
- Retention success rate when correctly targeted: 22%

If the model lifts correctly-targeted retention interventions such that 2 percentage points
of the lapsing book is saved, that is ~1,120 policies at €520 = **€582k retained annual
premium**, against roughly €40k of intervention cost on the targeted segment.

**Model objective**: expected value, not AUC. Rank policies by `P(lapse) × premium ×
P(save | contacted)` and take the top N where N is what the retention team can actually call.

## Quick Start (All-Local)

1. **Terraform the local stack**
   ```bash
   cd terraform && terraform init && terraform apply
   ```
2. **Bring up the compose stack** (Postgres + MLflow)
   ```bash
   docker compose -f ../docker/compose.local.yml up -d postgres mlflow
   ```
3. **Train** (writes to local MLflow at `http://localhost:5000`)
   ```bash
   docker compose -f docker/compose.local.yml --profile train run --rm train
   ```
4. **Serve**
   ```bash
   docker compose -f docker/compose.local.yml --profile serve up -d api
   ```
5. **Monitor**
   ```bash
   docker compose -f docker/compose.local.yml up -d monitoring   # Prometheus + Grafana
   ```

## Honest Risks

- This stack intentionally trades multi-node scale for zero-dependency local operation;
  a single host is a single point of failure (unless you spread the local inventories
  across VMs).
- Self-hosting every component means you own the upgrade/maintenance burden for each;
  that is the nature of an all-local platform and matches on-prem requirements.
- The ML artifact set here is synthetic/demo in nature — treat the data as illustrative.