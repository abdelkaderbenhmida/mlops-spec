# Ferry — Cloud-Portable ML Platform for EU Financial Services (DORA)

> **Target product name: Ferry** — a provably portable ML platform for EU financial
> services operating under DORA cloud-concentration and exit-strategy requirements.

## Overview

Build a real ML pipeline (train → track → serve → monitor) that runs **identically on two
cloud providers**, where **portability is continuously verified** — not asserted in a
document. Scope is intentionally tight: no enterprise overengineering, but the engineering
that exists must be defensible to a regulator, a security reviewer, and a CFO.

**The single testable promise of Ferry**:

> **The exit test is a CI job.** Any point in time, the platform can move 100% of traffic
> to the surviving provider within 4 hours (RTO), losing at most 15 minutes of data (RPO),
> and produce signed evidence that it did.

## Why Two Clouds: The Enterprise Problem

Multi-cloud is not free. It is a real cost paid for a real reason. A churn-model demo split
across two providers would be *strictly worse* than single-cloud: cross-cloud egress cost,
public-IP scraping, two IAM models, two Terraform state files, and a latency-exposed MLflow
dependency.

**Ferry exists because of one regulatory fact**:

**EU financial entities are legally required to prove they can leave a cloud provider.**

The Digital Operational Resilience Act (DORA) has applied to EU banks, insurers, and
investment firms since January 2025. Two of its requirements drive this platform directly:

- **Concentration risk (Art. 29).** Entities must assess and limit dependency on a single
  critical ICT third-party provider. A regulator can require an entity to reduce exposure
  where concentration is deemed excessive.
- **Exit strategies (Art. 28).** Contracts with critical ICT providers must include exit
  plans that are **documented and tested**, allowing the entity to leave without disrupting
  business continuity or breaching regulatory obligations.

**The gap**: Nearly every institution's "exit strategy" is a PowerPoint deck. It has never been
executed. Nobody knows how long it would take or whether it would work, because testing it
would mean rebuilding production somewhere else — which nobody has budget or appetite for.

Meanwhile the same institutions have concentrated their entire ML estate on one
hyperscaler's managed services (SageMaker, Vertex AI, Azure ML): precisely the services with
the deepest lock-in, because training jobs, feature definitions, registry, and serving are
all expressed in provider-proprietary APIs.

## Stack Components

### 1. Terraform — Infrastructure as Code
- **What**: IaC with shared module interface, per-provider implementations
- **How**: Shared module interface under `terraform/modules/`; `terraform/gcp/` and 
  `terraform/oracle/` are thin provider implementations of the same interface; separate 
  state per provider; no hardcoded credentials
- **Key files**: `terraform/modules/`, `terraform/gcp/`, `terraform/oracle/`, 
  `terraform/control/`, `terraform/network/`, `terraform/security-groups/`, 
  `terraform/compute/`
- **Usage**: `terraform apply` provisions identical stack on both providers from shared modules
- **Enterprise justification**: Same module interface, swappable provider implementation; 
  the portability mechanism

### 2. Ansible — Configuration Management
- **What**: Provider-neutral configuration; same playbook runs against both provider groups
- **How**: Dynamic inventory populated from Terraform outputs; all roles idempotent; 
  config parity verified, not assumed — same playbook runs against both provider groups,
  and a post-run check compares installed package versions, kubeadm/kubelet versions, and 
  rendered config files across the two clusters
- **Key files**: `ansible/roles/`, `ansible/inventory/`, `ansible/playbooks/`
- **Usage**: `ansible-playbook site.yml`
- **Enterprise justification**: Config parity is verified, not assumed; divergence fails the 
  drill readiness check; the same playbook runs against both provider groups

### 3. Kubernetes (kubeadm) — Self-Managed Orchestration
- **What**: Self-managed K8s on both providers (not GKE/EKS/Vertex AI/SageMaker)
- **How**: kubeadm 1.28, kubelet, kubectl; disable swap; init CP with 
  `--pod-network-cidr=192.168.0.0/16`; Calico CNI; identical roles, identical versions
  — this is what makes the parity test meaningful
- **Key files**: `kubernetes/`, `helm/`
- **Usage**: `kubectl get nodes`, `helm upgrade`, `kubectl rollout restart`
- **Enterprise justification**: The *only* way to keep the orchestration layer identical 
  across providers; a managed control plane is provider-specific by definition

### 4. Helm — Package Management
- **What**: Helm charts with per-provider values files
- **How**: Same chart deployed on both providers with per-provider `values-*.yaml`; 
  raw manifests mean copy-paste divergence — divergence is the failure mode this platform
  exists to prevent
- **Key files**: `helm/lapse-api/`, `values-gcp.yaml`, `values-oci.yaml`
- **Usage**: `helm upgrade --values values-gcp.yaml && helm upgrade --values values-oci.yaml`
- **Enterprise justification**: Two environments with per-provider differences is exactly 
  what values files solve; raw manifests mean copy-paste divergence

### 5. S3-Compatible Object Storage
- **What**: Artifact storage that works against GCS interop, OCI Object Storage, MinIO
- **How**: Never local disk, never provider-proprietary artifact APIs; GCS interop / OCI 
  Object Storage / MinIO
- **Key files**: `portability-contract.yaml`, MLflow control plane configuration
- **Usage**: MLflow artifact store; Helm chart values
- **Enterprise justification**: Provider KMS is forbidden by the contract; use a self-hosted, 
  provider-neutral store, or Sealed Secrets with keys held outside both clouds

### 6. mTLS — Cert-Manager
- **What**: mTLS between services via cert-manager
- **How**: cert-manager-issued certificates; a compromised network position is not sufficient 
  access; provider KMS is forbidden by the contract
- **Key files**: `kubernetes/`, `cert-manager/` configuration
- **Usage**: Mutual TLS between services; certificates issued by cert-manager in-cluster
- **Enterprise justification**: A compromised network position is not sufficient access; mTLS 
  via cert-manager covers the actual requirement; a service mesh across two self-managed 
  clusters is a large operational burden for marginal gain

### 7. CI/CD — Jenkins
- **What**: Docker container on the neutral control plane
- **How**: Pipeline on push to `main`; stages: checkout → portability check → test → train → 
  build → push → deploy (both providers) → post-deploy check; portability check parses 
  Terraform plans and Kubernetes manifests and **fails the build** on any forbidden dependency
- **Key files**: `jenkins/Jenkinsfile`, `jenkins/portability-check.groovy`
- **Usage**: Triggered on push to `main`; portability check also runs on every PR
- **Enterprise justification**: CI that runs anywhere, including on-prem, during an actual exit;
  the pipeline fails if `evaluate.py` exits 1 (expected-value gate) or if the portability
  check finds a forbidden dependency

### 8. mTLS — Between Services
- **What**: Mutual TLS between all services
- **How**: cert-manager-issued certificates between services; provider KMS is forbidden by 
  the contract; keys held outside both clouds
- **Key files**: `kubernetes/`, `cert-manager/` configuration
- **Enterprise justification**: A compromised network position is not sufficient access; 
  mTLS via cert-manager covers the actual requirement

### 9. IPsec — Cross-Cloud Networking
- **What**: Site-to-site IPsec between GCP VPC and OCI VCN
- **How**: Native on both providers; a few dozen lines of Terraform; non-overlapping CIDRs: 
  GCP `10.10.0.0/16`, OCI `10.20.0.0/16`; no service is reachable by public IP allowlist alone
- **Key files**: `terraform/ipsec/`, `terraform/gcp/`, `terraform/oracle/`
- **Usage**: IPsec tunnel between control plane and both clusters; all control plane traffic
- **Enterprise justification**: Cross-cloud data transfer is billed per gigabyte and is a 
  recurring cost; federation is not just cleaner, it is cheaper; metrics traversing the 
  public internet, authenticated only by source IP, is not acceptable

### 10. Prometheus Federation
- **What**: Per-provider local Prometheus; central Grafana federates aggregated series
- **How**: Each provider runs a local Prometheus that scrapes only its own cluster; central 
  instance federates aggregated series; cuts cross-cloud traffic by roughly an order of 
  magnitude; removes tight coupling where a network blip on one side blanks the other side's
  dashboards
- **Key files**: `monitoring/federation.yml`, `monitoring/prometheus/`
- **Enterprise justification**: Cuts cross-cloud data transfer costs; removes tight coupling;
  a network blip on one side does not blank the other side's dashboards

### 11. k6 — Load Testing
- **What**: Load testing against each provider independently
- **How**: `monitoring/k6/loadtest.js` runs against each provider independently; 20 virtual 
  users, 2 minutes; 70% GET /health, 30% POST /score; thresholds: http_req_duration p(95) 
  < 1000ms, http_req_failed < 1%
- **Key files**: `monitoring/k6/loadtest.js`
- **Enterprise justification**: Run once per provider; the exit drill re-runs this suite 
  against the surviving provider only

### 12. Sealed Secrets
- **What**: Provider-neutral secrets encryption
- **How**: Kubernetes Secrets are base64, not encryption; provider KMS violates the portability 
  contract; use Sealed Secrets with keys held outside both clouds, or a self-hosted, 
  provider-neutral store
- **Key files**: `kubernetes/`, `sealed-secrets/` configuration
- **Enterprise justification**: Keep a neutral one; Kubernetes Secrets are base64, not 
  encryption; provider KMS violates the portability contract

## Repository Structure

```
ferry/
├ terraform/                    # shared module interface, per-provider implementations
├ ansible/                      # dynamic inventory from Terraform outputs
├ helm/                         # lapse-api chart + per-provider values files
├ portability-contract.yaml     # enforced in CI
├ kubernetes/                   # cert-manager, nginx-ingress, sealed-secrets bootstrap
├ docker/                       # api/Dockerfile
├ ml/                           # data, train.py, evaluate.py, preprocess.py,
│   retention_feedback.py
├ api/                          # main.py, model.py, schemas.py, db.py, requirements.txt
├ jenkins/                      # Jenkinsfile, portability-check.groovy
├ exit-drills/                  # run-drill.sh, report generator
├ monitoring/                   # per-provider prometheus, federation.yml, grafana,
│   dashboards, k6/
│   └── loadtest.js
├── docs/                       # architecture.md, deployment.md
└── portability-contract.yaml   # forbidden dependencies + required abstractions
```

## Portability Contract

```yaml
# portability-contract.yaml
forbidden_dependencies:
  - managed_kubernetes          # GKE, EKS, OKE control planes
  - provider_ml_platform        # Vertex AI, SageMaker, Azure ML
  - provider_managed_database   # Cloud SQL, RDS, Autonomous DB
  - provider_serverless         # Cloud Run, Lambda, Functions
  - provider_specific_iam_in_app_code

required_abstractions:
  object_storage: s3_api          # works against GCS interop, OCI Object Storage, MinIO
  container_registry: oci_distribution_spec
  secrets: kubernetes_secrets     # not Secret Manager, not KMS-specific
  ingress: nginx_ingress          # not provider LB controllers
  identity: oidc                  # not provider-native service accounts in app code

exit_objectives:
  rto_hours: 4       # time to full traffic on the surviving provider
  rpo_minutes: 15    # tolerable data loss
```

A CI job parses Terraform plans and Kubernetes manifests and **fails the build** on any
forbidden dependency. Portability that is not enforced in CI decays within one sprint,
because the fastest path to shipping any given feature is always the managed service.

## Cloud Split — Symmetric, Not Asymmetric

Both providers run the **same stack**. Both have a Kubernetes cluster. Both serve
production traffic. Traffic distribution is a routing decision, not an architectural one.

| Cloud | Role |
|---|---|
| **Google Cloud (GCP)** | Primary serving — self-managed Kubernetes (kubeadm), lapse API, Postgres |
| **Oracle Cloud (OCI)** | Secondary serving — self-managed Kubernetes (kubeadm), lapse API, Postgres |

**The 80/20 split is deliberate**. A cold standby is not a tested exit path — it is another
untested document. Continuously serving 20% of real traffic from the secondary provider
means the exit path is exercised every single day, and any drift between environments
surfaces immediately rather than during an emergency.

## Networking Between Clouds — Done Properly

- **Site-to-site IPsec** between the GCP VPC and OCI VCN (native on both providers; a few
  dozen lines of Terraform). Non-overlapping CIDRs: GCP `10.10.0.0/16`, OCI `10.20.0.0/16`.
- **mTLS between services** (cert-manager), so a compromised network position is still not
  sufficient access.
- **Prometheus federation instead of cross-cloud scraping**: each provider runs a local
  Prometheus that scrapes only its own cluster; a central instance federates aggregated
  series. This cuts cross-cloud traffic by roughly an order of magnitude and removes the
  tight coupling where a network blip on one side blanks the other side's dashboards.

Egress pricing is the reason this matters commercially as well as architecturally.
Cross-cloud data transfer is billed per gigabyte and is a recurring cost that naive designs
discover only after the first invoice. Federation is not just cleaner, it is cheaper.

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

**Model objective**: expected value, not AUC. Optimise expected value at a fixed intervention
budget: rank policies by `P(lapse) × premium × P(save | contacted)` and take the top N
where N is what the retention team can actually call.

## Cost Model

| Line item | Single cloud | Ferry (dual) | Delta |
|---|---|---|---|
| Compute (3 nodes primary) | €340/mo | €340/mo | — |
| Compute (3 nodes secondary) | — | €300/mo | +€300 |
| Cross-cloud egress (with federation) | — | €45/mo | +€45 |
| VPN tunnels | — | €70/mo | +€70 |
| Operational overhead | 1.0 FTE-equivalent | 1.3 FTE-equivalent | +0.3 FTE |
| **Infrastructure subtotal** | **€340/mo** | **€755/mo** | **+€415/mo** |

Roughly **2.2× infrastructure cost and 1.3× operational load**. State this openly. A vendor
who claims multi-cloud is free is not credible.

Set against it:
- Tested DORA exit evidence, versus a remediation finding that costs materially more than
  €5k/year to close.
- Negotiating leverage at contract renewal on a spend where single-digit percentage
  concessions dwarf the delta.
- Genuine provider-outage resilience, which single-cloud multi-AZ does not provide.

## Exit Drill

Monthly, automatically, in business hours with the team watching:

```
T+0     Freeze deploys. Snapshot state. Announce drill start.
T+2m    Shift DNS: GCP 80/20 → 0/100 OCI.
T+5m    Verify: p95 latency, error rate, prediction volume, model version served.
T+10m   Run the full k6 suite against OCI only. HPA must scale.
T+20m   Verify MLflow registry reachable, model reload works, training job can start.
T+30m   Run a scoring-parity test: 10,000 stored feature vectors scored on both
        providers must produce identical predictions to floating-point tolerance.
T+45m   Restore 80/20. Confirm recovery.
T+50m   Generate signed Exit Drill Report.
```

**The T+30m parity test is the detail that makes this credible rather than theatrical.**
Failover that serves traffic but produces *different predictions* — because of library
version skew, a different base image, or a stale model on the secondary — is a silent
correctness failure far worse than an outage. Outages page someone. Wrong answers do not.

**Exit Drill Report artifact**:

```
exit-drills/2026-08-15/
├ summary.json           # RTO achieved, RPO achieved, pass/fail per objective
├ traffic_timeline.png   # requests/sec per provider through the drill
├ latency_comparison.md  # p50/p95/p99 on each provider, before and during
├ parity_report.json     # 10,000 predictions compared, max delta observed
├ failures.md            # anything that broke, with remediation owner and due date
└ manifest.json          # SHA-256 of every file, signed
```

Twelve of these per year is not a slide deck. It is evidence. **Drills must be allowed to
fail** — a drill failure is the product working correctly; remediation items from a failed
drill are tracked to completion with an owner and due date.

## Honest Risks

- Portability has a real ceiling; Kubernetes, containers, and Terraform port well but
  managed database features, IAM semantics, network behaviour, and storage performance
  characteristics do not.
- Operational complexity is the actual failure mode, not cost; two clusters means two
  upgrade cycles, two sets of certificates, two node-pool patch schedules.
- Teams that adopt multi-cloud without staffing for it end up with one well-maintained
  cluster and one that quietly rots — which is worse than single-cloud, because it
  produces false confidence.
- Drills must be allowed to fail; the instant the exit drill becomes a metric someone is
  judged on, it will be gamed into always passing.
- DORA is a European regulation; the same architecture is defensible elsewhere on
  resilience and negotiating-leverage grounds, but do not transplant the compliance
  argument verbatim into a US or APAC pitch.