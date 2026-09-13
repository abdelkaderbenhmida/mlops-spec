# Enterprise Upgrade — From "Two Clouds Because It Looks Impressive" to a Cloud-Portable ML Platform

> Target product name: **Ferry** — a provably portable ML platform for EU financial services
> operating under DORA cloud-concentration and exit-strategy requirements.
>
> This document rewrites `mlops-platform-spec.md`. The infrastructure choices stay almost
> identical: Terraform, Ansible, self-managed Kubernetes, MLflow, FastAPI, Jenkins,
> Prometheus/Grafana, k6, and a split across two cloud providers. What changes is the answer
> to the question a reviewer will always ask: **"why two clouds?"**

---

## 1. The question the original spec cannot answer

The original is a well-constructed multi-cloud build: GCP runs Kubernetes and inference, OCI
runs training, MLflow, and monitoring. Everything is Terraformed, Ansible-configured, and
load-tested. The acceptance criteria are sharp and testable.

But the multi-cloud split has no stated business reason. It reads as "I wanted to show I can
use two providers." An interviewer or a buyer will immediately note that this design is
*strictly worse* than single-cloud for a churn model: it adds cross-cloud egress cost,
public-IP scraping instead of private networking, two IAM models, two Terraform state files,
and a latency-exposed MLflow dependency across the public internet.

Multi-cloud is not free. It is a real cost you pay for a real reason. The upgrade is to name
that reason and then design *for* it, at which point every awkward part of the original
architecture becomes a deliberate, defensible choice.

---

## 2. The enterprise problem

**EU financial entities are now legally required to prove they can leave a cloud provider.**

The Digital Operational Resilience Act (DORA) has applied to EU banks, insurers, and
investment firms since January 2025. Two of its requirements drive this platform directly:

- **Concentration risk (Art. 29).** Entities must assess and limit dependency on a single
  critical ICT third-party provider. A regulator can require an entity to reduce exposure
  where concentration is deemed excessive.
- **Exit strategies (Art. 28).** Contracts with critical ICT providers must include exit
  plans that are **documented and tested**, allowing the entity to leave without disrupting
  business continuity or breaching regulatory obligations.

The gap: nearly every institution's "exit strategy" is a PowerPoint deck. It has never been
executed. Nobody knows how long it would take or whether it would work, because testing it
would mean rebuilding production somewhere else, which nobody has budget or appetite for.

Meanwhile the same institutions have concentrated their entire ML estate on one hyperscaler's
managed services — SageMaker, Vertex AI, Azure ML — which are precisely the services with the
deepest lock-in, because the training jobs, feature definitions, registry, and serving layer
are all expressed in provider-proprietary APIs.

**Ferry is an ML platform where the exit test is a CI job.** Portability is not asserted in a
document; it is continuously verified.

---

## 3. Why this justifies every original design decision

This is the satisfying part. Choices that looked like unnecessary hard mode in the original
spec become the product's core value:

| Original choice | Looked like | Actually is |
|---|---|---|
| Self-managed kubeadm, not GKE/EKS | Doing it the hard way | The *only* way to keep the orchestration layer identical across providers. A managed control plane is provider-specific by definition |
| MLflow instead of Vertex AI / SageMaker | Cheaper open source | Registry and tracking that move with you; the model registry is the hardest thing to migrate |
| Terraform with per-provider modules | Standard practice | The portability mechanism — same module interface, swappable provider implementation |
| Ansible for everything above the VM | Old-fashioned | Provider-neutral configuration; cloud-init and managed node pools are not |
| Jenkins in a container, not a managed CI service | Avoiding cost | CI that runs anywhere, including on-prem, during an actual exit |
| Two clouds simultaneously | Showing off | The exit path is *permanently warm*, not theoretical |
| Public-IP allowlisting between clouds | A shortcut | Honest about the cost of cross-cloud networking — see §6 where this gets fixed properly |

Nothing in the original stack needs replacing. It needs a thesis.

---

## 4. Who pays

| Buyer | Their pain | Trigger |
|---|---|---|
| CIO / Head of Cloud, EU bank or insurer | Regulator asked for evidence the exit plan works; there is none | DORA supervisory review, or a joint examination team request |
| Chief Risk Officer | Concentration risk register lists "all ML on one provider" with no mitigation | Annual risk assessment |
| Head of Infrastructure | Renewal negotiation with a hyperscaler where the institution has zero credible walk-away | Contract renewal cycle |
| FinOps lead | Committed-use discounts locked to one provider; no leverage, no arbitrage | Budget pressure |

The commercial argument has two halves, and the second one is what actually closes deals:

**Compliance:** produce tested exit evidence instead of an untested document.

**Negotiating leverage:** an institution that can demonstrably move its ML workload in
days negotiates its cloud contract from a completely different position. Hyperscaler
committed-use agreements at enterprise scale run into eight figures annually. A few
percentage points of discount, won because the walk-away threat is credible, pays for this
platform many times over. This is the argument the CFO understands.

---

## 5. The ML workload, made real

Replace the generic Telco churn dataset with a workload that carries actual money and fits
the buyer profile.

**Use case: policy lapse and renewal-risk prediction for a European general insurer.**

Why this fits better than telecom churn:

- The buyer is already in scope for DORA — same room, same budget.
- The economics are unambiguous and the insurer already tracks them.
- It is a genuinely hard prediction problem with real seasonality and price sensitivity,
  not a toy dataset with a 0.85 AUC ceiling.

**The business loop:**

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

**Economics that make the model's value calculable:**

| Quantity | Typical value | Notes |
|---|---|---|
| Book size | 400,000 active policies | Mid-size regional insurer |
| Average annual premium | €520 | Motor/home mix |
| Baseline annual lapse rate | 14% | ~56,000 lapsing policies |
| Retention offer cost | €35 average | Discount plus contact cost |
| Retention success rate when correctly targeted | 22% | Industry-plausible |

If the model lifts correctly-targeted retention interventions such that 2 percentage points
of the lapsing book is saved, that is ~1,120 policies at €520 = **€582k retained annual
premium**, against roughly €40k of intervention cost on the targeted segment. The
sensitivity that matters is *precision*, because intervention cost scales with how many
policies you contact — a model that flags everyone as high-risk destroys the economics even
if its recall is perfect.

**This changes the model objective.** Do not optimise AUC. Optimise **expected value at a
fixed intervention budget**: rank policies by `P(lapse) × premium × P(save | contacted)` and
take the top N where N is what the retention team can actually call. That framing — capacity-
constrained ranking rather than classification — is what separates someone who has deployed
a model into a business process from someone who has run `train_test_split`.

---

## 6. Architecture changes

### 6.1 Symmetric, not asymmetric

The original is asymmetric: GCP serves, OCI trains. That means OCI has never proven it can
serve, so the exit test would fail exactly when it matters.

**Ferry runs the same stack on both providers.** Both have a Kubernetes cluster. Both can
serve. Traffic distribution is a routing decision, not an architectural one.

```
                             ┌──────────────────┐
                             │   Global DNS /   │
                             │  health-checked  │
                             │     routing      │
                             └────┬────────┬────┘
                    weight: 80%   │        │  weight: 20%
                    ┌─────────────▼──┐  ┌──▼──────────────┐
                    │   GCP region   │  │   OCI region    │
                    │  ┌──────────┐  │  │  ┌──────────┐   │
                    │  │ k8s (3n) │  │  │  │ k8s (3n) │   │
                    │  │ lapse-api│  │  │  │ lapse-api│   │
                    │  │ postgres │  │  │  │ postgres │   │
                    │  └──────────┘  │  │  └──────────┘   │
                    └────────┬───────┘  └───────┬─────────┘
                             │                  │
                             └────────┬─────────┘
                                      │
                        ┌─────────────▼──────────────┐
                        │   Control plane (neutral)   │
                        │  MLflow · registry · Jenkins│
                        │  artifacts on S3-compatible │
                        │  object storage             │
                        └─────────────────────────────┘
```

The 80/20 split is deliberate. A cold standby is not a tested exit path — it is another
untested document. Continuously serving 20% of real traffic from the secondary provider
means the exit path is exercised every single day, and any drift between environments
surfaces immediately rather than during an emergency.

### 6.2 The Portability Contract

A machine-checkable definition of what "portable" means. This is the specification's core
technical artifact.

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
forbidden dependency. Portability that is not enforced in CI decays within one sprint, because
the fastest path to shipping any given feature is always the managed service.

### 6.3 The Exit Drill

The product's signature capability. A scheduled, automated, evidence-producing failover.

```
Monthly, automatically, in business hours with the team watching:

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

The scoring-parity test at T+30m is the detail that makes this credible rather than
theatrical. Failover that serves traffic but produces *different predictions* — because of a
library version skew, a different base image, or a stale model on the secondary — is a silent
correctness failure far worse than an outage. Outages page someone. Wrong answers do not.

**The Exit Drill Report** is what the institution hands the regulator:

```
exit-drills/2026-08-15/
├── summary.json           # RTO achieved, RPO achieved, pass/fail per objective
├── traffic_timeline.png   # requests/sec per provider through the drill
├── latency_comparison.md  # p50/p95/p99 on each provider, before and during
├── parity_report.json     # 10,000 predictions compared, max delta observed
├── failures.md            # anything that broke, with remediation owner and due date
└── manifest.json          # SHA-256 of every file, signed
```

Twelve of these per year is not a slide deck. It is evidence.

### 6.4 Networking, done properly

The original allows OCI Prometheus to scrape GCP node exporters over public IPs with IP
allowlisting, and calls a VPN unnecessary. For a portfolio lab that is a reasonable
simplification. For a financial institution it will not survive the first security review —
metrics traversing the public internet, authenticated only by source IP, is not acceptable.

Fix it, and note that fixing it is cheap:

- **Site-to-site IPsec** between the GCP VPC and OCI VCN. Both providers offer this natively;
  it is a few dozen lines of Terraform. Non-overlapping CIDRs: GCP `10.10.0.0/16`,
  OCI `10.20.0.0/16`.
- **mTLS between services**, so a compromised network position still is not sufficient access.
- **Prometheus federation** rather than cross-cloud scraping: each provider runs a local
  Prometheus, and a central instance federates aggregated series. This cuts cross-cloud
  traffic by roughly an order of magnitude and removes the tight coupling where a network
  blip on one side blanks the other side's dashboards.

Egress pricing is the reason this matters commercially as well as architecturally. Cross-cloud
data transfer is billed per gigabyte and is a recurring cost that naive designs discover only
after the first invoice. Federation is not just cleaner, it is cheaper.

---

## 7. What the original said not to build — revisited

The original's "What NOT to Build" list is one of its strongest sections; scope discipline is
rare. Three items should now move, and the rest should stay excluded.

| Item | Original | Revised | Why |
|---|---|---|---|
| Helm | Excluded, raw manifests | **Include** | Two environments with per-provider differences is exactly the problem Helm values files solve. Raw manifests mean copy-paste divergence, and divergence is the failure mode this platform exists to prevent |
| External secrets manager | Excluded | **Include a neutral one** | Kubernetes Secrets are base64, not encryption. But using each provider's KMS violates the portability contract. Use a self-hosted, provider-neutral secrets store, or Sealed Secrets with keys held outside both clouds |
| Canary deployment | Excluded | **Include** | The 80/20 traffic split infrastructure already gives you this for free; not using it for progressive delivery would be wasteful |
| DVC | Excluded | **Keep excluded initially** | Reintroduce when training data exceeds what fits comfortably in object storage with simple date-partitioned paths. Do not add it as decoration |
| Service mesh | Excluded | **Keep excluded** | mTLS via cert-manager covers the actual requirement. A mesh across two self-managed clusters is a large operational burden for marginal gain |
| Multi-region within a provider | Excluded | **Keep excluded** | Cross-provider redundancy already exceeds what single-provider multi-region gives you. Adding both is over-engineering |
| GPU instances | Excluded | **Keep excluded** | Tabular gradient boosting on 400k rows does not need a GPU. Adding one signals unfamiliarity with the workload |

---

## 8. Cost model

Concrete numbers, because "multi-cloud is expensive" is the first objection and it deserves a
real answer rather than hand-waving.

| Line item | Single cloud | Ferry (dual) | Delta |
|---|---|---|---|
| Compute (3 nodes primary) | €340/mo | €340/mo | — |
| Compute (3 nodes secondary) | — | €300/mo | +€300 |
| Cross-cloud egress (with federation) | — | €45/mo | +€45 |
| VPN tunnels | — | €70/mo | +€70 |
| Operational overhead | 1.0 FTE-equivalent | 1.3 FTE-equivalent | +0.3 FTE |
| **Infrastructure subtotal** | **€340/mo** | **€755/mo** | **+€415/mo** |

Roughly **2.2× infrastructure cost and 1.3× operational load.** State this openly. A vendor
who claims multi-cloud is free is not credible.

Set against it:

- Tested DORA exit evidence, versus a remediation finding that costs materially more than
  €5k/year to close.
- Negotiating leverage at contract renewal on a spend where single-digit percentage
  concessions dwarf the delta.
- Genuine provider-outage resilience, which single-cloud multi-AZ does not provide — regional
  and control-plane-wide incidents at every major provider are a matter of public record.

The honest framing: **this is insurance with a measurable premium.** For a regulated
institution the premium is worth it. For a startup it is not, and saying so builds more trust
than pretending otherwise.

---

## 9. Revised acceptance criteria

Keep every original criterion. They are good. Add:

- [ ] `terraform apply` provisions an identical stack on both providers from shared modules
- [ ] The portability-contract CI check fails the build on any provider-locked dependency
- [ ] Both clusters serve production traffic simultaneously at the configured weights
- [ ] The scoring-parity test passes: identical predictions across providers on 10,000 vectors
- [ ] A full exit drill completes within the 4-hour RTO objective, unattended
- [ ] The exit drill report generates automatically with a signed manifest
- [ ] Cross-cloud traffic runs over IPsec; no service is reachable by public IP allowlist alone
- [ ] Prometheus federation is in place; no cross-cloud raw scraping
- [ ] The lapse model is evaluated on expected value at fixed intervention capacity, not AUC alone
- [ ] Retention campaign outcomes feed back as labels within 60 days of scoring
- [ ] A deliberately failed drill is caught, reported, and produces a remediation item

The last one matters most. A system that has never reported a drill failure has almost
certainly never really been tested.

---

## 10. Implementation plan

| Phase | Deliverable | Days |
|---|---|---|
| 0 | Portability contract + CI enforcement job | 2 |
| 1 | Terraform shared module interface, both provider implementations | 4 |
| 2 | Ansible roles, verified byte-identical config on both providers | 3 |
| 3 | Kubernetes via kubeadm on both, Helm chart with per-provider values | 4 |
| 4 | Lapse model: data, expected-value objective, capacity-constrained ranking | 3 |
| 5 | MLflow control plane on neutral object storage, reachable from both | 2 |
| 6 | Serving API + Postgres on both providers | 3 |
| 7 | IPsec tunnels, mTLS, Prometheus federation | 3 |
| 8 | Weighted DNS routing, health checks, automated failover | 2 |
| 9 | Scoring-parity test harness | 2 |
| 10 | Exit drill automation + report generator | 3 |
| 11 | Jenkins pipeline deploying to both providers | 2 |
| 12 | k6 load testing against each provider independently | 2 |
| 13 | First full supervised exit drill + remediation | 2 |

**Total: ~37 days.**

---

## 11. Honest risks

**Portability has a real ceiling.** Kubernetes, containers, and Terraform port well. Managed
database features, IAM semantics, network behaviour, and storage performance characteristics
do not. Ferry makes the ML platform portable; it does not make the entire institution
portable, and claiming otherwise oversells it.

**Operational complexity is the actual failure mode**, not cost. Two clusters means two
upgrade cycles, two sets of certificates, two node-pool patch schedules. Teams that adopt
multi-cloud without staffing for it end up with one well-maintained cluster and one that
quietly rots — which is worse than single-cloud, because it produces false confidence. The
80/20 live-traffic split is the specific mitigation: a rotting secondary that serves real
customers gets noticed within hours.

**Drills must be allowed to fail.** The instant the exit drill becomes a metric someone is
judged on, it will be gamed into always passing. Failures found in a drill are the product
working correctly. This needs explicit executive framing before the first drill, not after
the first failure.

**DORA is a European regulation.** The same architecture is defensible elsewhere on
resilience and negotiating-leverage grounds, but do not transplant the compliance argument
verbatim into a US or APAC pitch. The equivalent hooks there are operational resilience
guidance and vendor concentration policy, and they carry less force.
