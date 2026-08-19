# Ferry — Cloud-Portable ML Platform for EU Financial Services (DORA)

A provably portable ML platform for **policy lapse and renewal-risk prediction** in
European financial services, provisioned with infrastructure-as-code across **two cloud
providers** and operated with Kubernetes, Helm, Ansible, and Jenkins.

Ferry answers the question every multi-cloud project gets asked — **"why two clouds?"** —
with one sentence: because EU financial entities are legally required to prove they can
leave a cloud provider (DORA Art. 28 exit strategies, Art. 29 concentration risk), and the
only credible proof is to do it — continuously, on real traffic, in CI.

> **The exit test is a CI job.** The platform can move 100% of traffic to the surviving
> provider within 4 hours (RTO, ≤15 min RPO) and produces signed evidence — an Exit Drill
> Report — every month.

## How it works

- **Symmetric architecture**: both GCP and OCI run identical self-managed Kubernetes
  clusters (kubeadm, no managed control planes) serving the lapse API. Traffic splits
  80/20 GCP/OCI via health-checked DNS, so the secondary's serving path is exercised every
  day, not just during drills.
- **Portability Contract** (`portability-contract.yaml`): a CI job fails the build on any
  provider-locked dependency (GKE/EKS/OKE, Vertex AI, SageMaker, Cloud SQL, provider
  serverless, provider IAM in app code).
- **MLflow on a neutral control plane** with S3-compatible artifact storage — the model
  registry is the hardest thing to migrate, so it is built to move.
- **Monthly Exit Drills**: automated failover to 0/100 OCI, full k6 suite, a scoring-parity
  test (10,000 vectors, identical predictions on both providers), and a signed report
  bundle for the regulator.
- **Networking that survives a security review**: site-to-site IPsec between the VPC and
  VCN, mTLS between services, Prometheus federation instead of cross-cloud scraping.
- **A model objective a CFO can price**: the lapse model optimizes **expected value at a
  fixed intervention budget** (`P(lapse) × premium × P(save | contacted)`, capacity-
  constrained ranking) — not AUC. Retention campaign outcomes feed back as labels within
  60 days.

## Cloud Split

| Cloud | Role |
|---|---|
| **Google Cloud (GCP)** | Primary serving — self-managed Kubernetes (kubeadm), lapse API, Postgres |
| **Oracle Cloud (OCI)** | Secondary serving — self-managed Kubernetes (kubeadm), lapse API, Postgres |

Cross-cloud traffic runs over **site-to-site IPsec** (GCP `10.10.0.0/16` ⇄ OCI
`10.20.0.0/16`) with mTLS between services. No service is reachable by public IP
allowlist alone. Monitoring uses **Prometheus federation**: each provider runs a local
Prometheus, central Grafana federates aggregated series.

## Stack

| Layer | Tool |
|---|---|
| Infrastructure-as-Code | Terraform (shared module interface, per-provider implementations) |
| Configuration management | Ansible (role-based, idempotent, byte-identical across providers) |
| Containers | Docker |
| Orchestration | Kubernetes (kubeadm 1.28, self-managed, Calico CNI) |
| K8s packaging | Helm (per-provider values files) |
| CI/CD | Jenkins (Docker container on the neutral control plane) |
| Experiment tracking | MLflow 2.10 (S3-compatible artifact store) |
| Model serving | FastAPI + Uvicorn |
| Database | PostgreSQL (StatefulSet per cluster) |
| Secrets | Sealed Secrets (keys outside both clouds) |
| mTLS | cert-manager |
| Metrics | Prometheus (per provider) + Grafana (federated) |
| Load testing | k6 |
| ML framework | scikit-learn (gradient boosting) |

## Repository Structure

```
ferry/
├── terraform/                 # modules/ (shared interface) + gcp/, oracle/, control/, ipsec/
├── ansible/                   # roles + playbooks, byte-identical on both providers
├── helm/
│   ├── lapse-api/             # chart: API, HPA, ingress, Postgres StatefulSet
│   ├── values-gcp.yaml
│   └── values-oci.yaml
├── portability-contract.yaml  # enforced in CI
├── kubernetes/                # cert-manager, nginx-ingress, sealed-secrets bootstrap
├── docker/api/                # FastAPI image
├── ml/                        # train/evaluate/preprocess/retention_feedback + data
├── api/                       # FastAPI: /health, /score, /predictions, /metrics
├── jenkins/                   # Jenkinsfile + portability-check job
├── exit-drills/               # automated drill driver + report generator
├── monitoring/                # per-provider Prometheus, federation, Grafana, k6
└── docs/
    ├── architecture.md
    └── deployment.md
```

## Deployment Order

```
1.  terraform apply (control/)   → neutral control plane (MLflow, Jenkins, S3-compatible storage)
2.  terraform apply (gcp/)       → GCP VPC + IPsec endpoint + 3 k8s VMs
3.  terraform apply (oracle/)    → OCI VCN + IPsec endpoint + 3 k8s VMs
4.  terraform apply (ipsec)      → tunnels up
5.  ansible-playbook site.yml    → byte-identical config on both providers, K8s initialized
6.  kubectl apply -f kubernetes/ → cert-manager, nginx-ingress, sealed-secrets bootstrap
7.  python ml/train.py           → lapse model trained, registered in MLflow
8.  helm upgrade values-gcp && values-oci → API + DB on both clusters
9.  Configure DNS 80/20 → GCP/OCI
10. Jenkins configured (manual, first time only)
11. k6 run loadtest.js           → validate performance + HPA on each provider
12. Run first supervised exit drill → baseline evidence + remediation list
```

See [docs/deployment.md](docs/deployment.md) for the full walkthrough.

## Why the cost is worth it

Multi-cloud is not free. Ferry costs roughly **2.2× infrastructure (+€415/mo) and 1.3×
operational load** versus single-cloud — stated openly in the spec. Set against it:
tested DORA exit evidence (vs. a remediation finding costing far more than €5k/year),
negotiating leverage at contract renewal on eight-figure hyperscaler spend, and genuine
provider-outage resilience. It is **insurance with a measurable premium** — for a regulated
institution the premium is worth it; for a startup it is not.

## Acceptance Criteria (highlights)

- [ ] Identical stack provisions on both providers from shared Terraform modules
- [ ] Portability-contract CI check fails the build on any provider-locked dependency
- [ ] Both clusters serve production traffic simultaneously at 80/20
- [ ] Scoring parity: identical predictions across providers on 10,000 vectors
- [ ] Full exit drill completes within the 4-hour RTO objective, unattended, with a signed report
- [ ] No service reachable by public IP allowlist alone; Prometheus federation only
- [ ] Lapse model gated on expected value at fixed intervention capacity, not AUC alone
- [ ] A deliberately failed drill is caught, reported, and produces a remediation item

Full criteria: see `mlops-platform-spec.md`.
