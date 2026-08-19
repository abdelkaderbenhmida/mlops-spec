# Deployment Guide

End-to-end deployment of **Ferry**, the cloud-portable ML platform for policy lapse and
renewal-risk prediction, following the order defined in
[`mlops-platform-spec.md` §Deployment Order](../mlops-platform-spec.md):

```
1.  terraform apply (control/)   → neutral control plane: MLflow, Jenkins, S3-compatible storage
2.  terraform apply (gcp/)       → GCP VPC + IPsec endpoint + 3 k8s VMs
3.  terraform apply (oracle/)    → OCI VCN + IPsec endpoint + 3 k8s VMs
4.  terraform apply (ipsec)      → tunnels up, both CIDRs non-overlapping
5.  ansible-playbook site.yml    → byte-identical config on both providers, K8s initialized
6.  kubectl apply -f kubernetes/ → cert-manager, nginx-ingress, sealed-secrets bootstrap
7.  python ml/train.py           → model trained, registered in MLflow ("lapse-model")
8.  helm upgrade values-gcp && values-oci → API + DB on both clusters
9.  Configure DNS 80/20 → GCP/OCI
10. Jenkins configured (manual, first time only)
11. k6 run loadtest.js           → validate performance + HPA on each provider
12. Run first supervised exit drill → baseline evidence + remediation list
```

> **Use case note.** This guide previously deployed a *Telco churn* model to a single
> serving cluster on GCP with OCI as training/monitoring only. Ferry is symmetric: both
> providers run identical clusters and both serve live traffic (80/20 split), so
> everything below runs **twice — once per provider** — against the *lapse* model.
>
> **Networking note.** The old guide relied on public-IP scraping and IP allowlisting
> between clouds ("no VPN required"). That design is superseded: cross-cloud traffic now
> runs over **site-to-site IPsec** with mTLS between services, and monitoring uses
> **Prometheus federation** instead of cross-cloud raw scraping.

---

## Prerequisites

| Tool | Version | Used for |
|---|---|---|
| Terraform | >= 1.5 | provisioning `terraform/gcp`, `terraform/oracle`, `terraform/control`, ipsec |
| Ansible | current | `ansible/playbooks/*.yml` |
| Python | 3.11 (recommended) | `ml/*` scripts |
| kubectl | 1.28 | cluster verification |
| helm | current | deploying `helm/lapse-api` |
| k6 | current | load testing |

Credentials you must have ready:

- **GCP**: project ID, a service account with Compute + VPN permissions
  (or Application Default Credentials), a public SSH key for the `ubuntu` user.
- **OCI**: tenancy OCID, user OCID, API key fingerprint, API private key PEM
  path, compartment OCID, region, and the same public SSH key.
- The SSH key is used by Terraform to inject `ubuntu:<public_key>` on GCP and
  `ssh_authorized_keys` on OCI, and by Ansible to connect.

> All credentials are supplied via variables/env — never commit them to the repo.

---

## 1. Provision the control plane (first)

The neutral control plane hosts MLflow, the model registry, Jenkins, and S3-compatible
artifact storage. It must exist before the clusters so training and model serving have a
registry to talk to, and it must be reachable from both clouds over the IPsec tunnel.

```bash
cd terraform/control
terraform init && terraform apply
```

Capture the outputs — the MLflow endpoint (`MLFLOW_TRACKING_URI`) and the control-plane
internal IP used in the IPsec routes.

## 2. Provision GCP and OCI (in any order — but both before IPsec)

Terraform state is separate per provider. Both provider stacks implement the same module
interface with non-overlapping CIDRs: GCP `10.10.0.0/16`, OCI `10.20.0.0/16`.

```bash
cd ../gcp
terraform init && terraform apply
# creates VPC 10.10.0.0/16, firewall (22, 6443, 30000–32767, 9100, IPsec UDP 500/4500),
# 3 VMs: gcp-k8s-cp (10.10.0.10), gcp-k8s-w1 (10.10.0.11), gcp-k8s-w2 (10.10.0.12)

cd ../oracle
terraform init && terraform apply
# creates VCN 10.20.0.0/16, security list (SSH + IPsec from GCP peer),
# 3 VMs: oci-k8s-cp (10.20.0.10), oci-k8s-w1 (10.20.0.11), oci-k8s-w2 (10.20.0.12)
```

Verify all six nodes plus the control plane are up and reachable over SSH as `ubuntu`.

## 3. Bring up the IPsec tunnels

```bash
cd ../ipsec
terraform init && terraform apply
```

This wires the GCP VPN gateway to the OCI DRG over site-to-site IPsec (UDP 500/4500),
with routes for `10.10.0.0/16` ⇄ `10.20.0.0/16` and the control plane's subnet.

**Verify:**

```bash
# from gcp-k8s-cp:
ping 10.20.0.10      # reachable across the tunnel, NOT via any public IP
ping <control-plane-ip>
```

**No service is reachable by public IP allowlist alone** — cross-cloud traffic is
tunnel-only.

---

## 4. Configure all servers with Ansible

The Ansible inventory is populated from Terraform outputs (static fallback with
placeholder IPs exists under `ansible/inventory/hosts.yml` — replace `ansible_host` values
if you use it). Run the master playbook:

```bash
cd ansible
ansible-playbook -i inventory/hosts.yml playbooks/site.yml
```

The master playbook runs, in order:

1. **all hosts**: `common` (timezone, base packages, node exporter, UFW) + `docker` (Docker CE).
2. **both k8s groups**: `kubernetes` — swap off, kubeadm 1.28, `kubeadm init --pod-network-cidr=192.168.0.0/16`, Calico CNI, workers joined, all nodes waited for `Ready`. **Identical roles, identical versions, both providers.**
3. **control-plane**: `mlflow` (MLflow + PostgreSQL containers, artifact store on S3-compatible storage) and `training` (Python 3.11 venv, deps, scripts).
4. **per-provider hosts**: `monitoring` (local Prometheus per provider + central Grafana federation).

Targeted playbooks are also available:

```bash
ansible-playbook -i inventory/hosts.yml playbooks/k8s.yml        # both clusters
ansible-playbook -i inventory/hosts.yml playbooks/ml.yml         # training + MLflow
ansible-playbook -i inventory/hosts.yml playbooks/monitoring.yml # Prometheus (per provider) + Grafana
```

**Config parity is verified, not assumed:** the playbook's post-run check compares
package versions, kubeadm/kubelet versions, and rendered config files across the two
clusters. Divergence fails the drill readiness check.

**Verify:**

```bash
ssh ubuntu@<gcp-cp-ip>  "kubectl get nodes -o wide"    # 3 nodes Ready
ssh ubuntu@<oci-cp-ip>  "kubectl get nodes -o wide"    # 3 nodes Ready
curl http://<control-plane-ip>:5000/health             # MLflow is alive
# Prometheus + Grafana reachable via control-plane federation
```

---

## 5. Bootstrap cluster add-ons (cert-manager, ingress, sealed secrets)

```bash
# from either control-plane host:
kubectl apply -f kubernetes/     # per cluster: cert-manager, nginx-ingress, sealed-secrets
```

- **cert-manager**: issues mTLS certificates between services.
- **nginx ingress**: the only ingress controller allowed (portability contract — no
  provider LB controllers).
- **Sealed Secrets**: secrets are encrypted at rest; the sealing keys live **outside
  both clouds**.

---

## 6. Train and register the model

Run training on the control plane:

```bash
ssh ubuntu@<control-plane-ip>
cd /opt/ml
/opt/ml-env/bin/python train.py
```

Locally (from the repo root, with MLflow reachable):

```bash
export MLFLOW_TRACKING_URI="http://<control-plane-ip>:5000"
python ml/train.py
```

`train.py` trains the lapse model on the policy book (~400k rows, date-partitioned),
ranks policies by expected value at the fixed intervention capacity, logs metrics
(including expected value at budget and precision@N — **not AUC alone**), registers the
model as **`lapse-model`** in the MLflow Model Registry, and saves the artifact to
S3-compatible storage.

**Verify:** open `http://<control-plane-ip>:5000`, confirm the run under experiment
`policy-lapse` and the registered model `lapse-model` version 1.

Run the CI gate locally to confirm it passes:

```bash
export MLFLOW_TRACKING_URI="http://<control-plane-ip>:5000"
python ml/evaluate.py      # exits 0 if expected value >= gate, else 1
```

The feedback loop (`ml/retention_feedback.py`) ingests campaign outcomes and publishes
them as labels within 60 days of scoring.

---

## 7. Deploy the API and database to both clusters (Helm)

From a control-plane host with kubeconfigs for both clusters:

```bash
helm upgrade --install lapse-api helm/lapse-api --values helm/values-gcp.yaml --kubeconfig <gcp-kubeconfig>
helm upgrade --install lapse-api helm/lapse-api --values helm/values-oci.yaml --kubeconfig <oci-kubeconfig>
```

`helm/lapse-api` contains the API Deployment (2 replicas, probes on `/health`), Service,
HPA (2–8 replicas at 60% CPU), nginx Ingress, and the PostgreSQL StatefulSet + PVC +
Sealed Secret. Per-provider values differ only in cluster-specific endpoints — the chart
is identical, which is the point.

Set `MLFLOW_TRACKING_URI` in the values file to `http://<control-plane-internal-ip>:5000`
(the tunnel address, not a public IP).

**Verify — on both providers:**

```bash
kubectl -n mlops get pods          # 2x lapse-api Running/Ready
kubectl -n mlops get deploy,svc,hpa,pvc
curl http://<gcp-ingress>/health   # {"status":"ok","model_version":"1","cluster":"gcp"}
curl http://<oci-ingress>/health   # {"status":"ok","model_version":"1","cluster":"oci"}
```

Exercise the API on both:

```bash
curl -X POST http://<ingress>/score \
  -H "Content-Type: application/json" \
  -d '{"policy_id":"P-4839201","tenure_months":28,"annual_premium":520.0,
       "product_line":"home","prior_claims":0,"renewal_date":"2026-09-15"}'
# {"lapse_probability":0.31,"expected_value":41.2,"bucket":"medium"}

curl "http://<ingress>/predictions?limit=5"   # rows from local PostgreSQL
```

---

## 8. Configure traffic split (80/20)

Point global DNS at both ingresses with health checks, weight 80% to GCP and 20% to OCI.
The health-checked routing is what makes the exit drill a routing decision rather than a
rebuild.

**Verify:** watch the traffic-share panel in Grafana — both providers must be serving, at
the configured weights, continuously.

---

## 9. Jenkins first-time setup (manual)

Jenkins runs as a Docker container **on the control plane**, triggered on push to `main`.
First-time, manual setup:

1. Start the Jenkins container on the control plane (Docker is already installed by the
   `docker` role).
2. Unlock Jenkins with the initial admin password from the container logs.
3. Add credentials to the Jenkins credential store:
   - **Docker Hub** credentials (for `docker build`/`docker push`),
   - **kubeconfigs for both clusters** as secret files,
   - **OCI/GCP SSH keys** as SSH credentials.
4. Create a pipeline job pointing at the repo's `Jenkinsfile`, with a webhook so a push
   to `main` triggers the pipeline.

Pipeline stages (per spec): Checkout → **Portability check** (fails on any
provider-locked dependency) → Test (`pytest api/` + `python ml/evaluate.py` EV gate) →
Train (control plane) → Build → Push → **Deploy GCP + Deploy OCI** (helm upgrade each) →
post-deploy health check on both. The build **fails** if `evaluate.py` exits 1 or the
portability check trips.

---

## 10. Load test with k6 — per provider

Run the suite against **each provider independently**:

```bash
k6 run monitoring/k6/loadtest.js --env API_URL=http://<gcp-ingress>:80
k6 run monitoring/k6/loadtest.js --env API_URL=http://<oci-ingress>:80
```

The test: 20 virtual users for 2 minutes, 70% `GET /health`, 30% `POST /score`, with
thresholds `http_req_duration p(95) < 1000ms` and `http_req_failed < 1%`. Watch Grafana
(ML API dashboard, per-provider panels) and HPA behavior while it runs.

**Verify:**

```bash
kubectl -n mlops get hpa          # CPU utilization climbing; replicas 2 → up to 8
```

---

## 11. Run the first exit drill

Monthly, automatically, in business hours with the team watching. `exit-drills/run-drill.sh`
drives it:

```bash
bash exit-drills/run-drill.sh
```

Timeline: freeze deploys → shift DNS 0/100 to OCI → verify latency/error/prediction
volume → full k6 suite against OCI (HPA must scale) → verify MLflow reachable + model
reload → **scoring-parity test (10,000 vectors, identical predictions to
floating-point tolerance on both providers)** → restore 80/20 → generate signed report.

Output lands in `exit-drills/<date>/` with `summary.json`, `traffic_timeline.png`,
`latency_comparison.md`, `parity_report.json`, `failures.md` (owner + due date), and a
signed `manifest.json`. **First drill is supervised**; after the remediation list from it
is closed, drills run unattended.

> A drill that fails is the product working correctly. Failures produce remediation
> items — never silence.

---

## Acceptance checkpoints

| Check | Command |
|---|---|
| 6 nodes + control plane provisioned | `terraform output` in each provider dir |
| Both clusters healthy | `kubectl get nodes` → 3 nodes `Ready` on each |
| Tunnel up | `ping 10.20.0.10` from GCP (no public IPs) |
| Model registered | MLflow UI at `http://<control-plane-ip>:5000` → `lapse-model` |
| Scores work | `curl POST /score` + `GET /predictions` on **both** providers |
| Monitoring live | Grafana shows per-provider node + API + ML dashboards (federation only) |
| Traffic split | Grafana traffic-share panel ≈ 80/20 |
| HPA scales | `kubectl -n mlops get hpa` during k6 on each provider |
| CI green | Jenkins pipeline on push to `main`, both deploys, portability check green |
| k6 within budget | p95 < 1000 ms, error rate < 1%, per provider |
| Parity | `parity_report.json` max delta within floating-point tolerance |
| No hardcoded secrets | `rg -i "password\|secret" --glob '!*.md'` → env/secret references only |

---

## Troubleshooting

### Terraform / IPsec

- **`terraform apply` hangs creating OCI instances** — OCI micro-shape availability
  varies by AD/region. Set `availability_domain` in the VM module call if the
  auto-detected first AD is full.
- **Provider credentials rejected** — confirm OCI `fingerprint`/`private_key_path` match
  the API key uploaded to the user, and that the GCP service account has the needed
  Compute/VPN permissions.
- **Tunnel down** — check UDP 500/4500 both directions and that the peer CIDRs match the
  route tables on each side. A firewall that allows the tunnel only one way is a common
  first failure.

### Ansible

- **`ansible-playbook site.yml` fails to connect** — `ansible/inventory/hosts.yml` static
  fallback has placeholder IPs; replace `ansible_host` values with real IPs from
  `terraform output`, and confirm the SSH key path.
- **Re-run safety** — all roles are idempotent; re-running the playbook is safe.
- **kubeadm init needs a working kubelet** — the role disables swap, loads
  `overlay`/`br_netfilter`, and configures containerd's systemd cgroup driver before
  init; if init fails on cgroup errors, check `docker info` for `cgroup driver` = systemd
  on every node.
- **Worker join fails** — the join command is generated on each CP; ensure port 6443 is
  reachable from that provider's workers.
- **node exporter not scraped** — each provider's Prometheus scrapes only its own VMs;
  if a target is down, check the local firewall, not the other cloud's rules.

### ML / API

- **`train.py` can't find the data** — it defaults to `ml/data/policies.csv` relative to
  the working directory; on the control plane run from `/opt/ml`. Override with
  `POLICIES_DATA_PATH`.
- **`evaluate.py` exits 1** — expected value at budget below the gate; retrain or accept
  the lower model. The gate is intentional CI behavior. (Note: the gate is on expected
  value, not AUC.)
- **API pods crash-looping at startup** — the app fails if MLflow is unreachable
  (`load_model()` raises) or PostgreSQL isn't up. Confirm `MLFLOW_TRACKING_URI` points at
  the control plane's **tunnel** address and the tunnel is up.
- **HPA never scales** — CPU-based autoscaling requires the Kubernetes **metrics-server**;
  install it in each cluster if absent.
- **Scores differ between providers (parity failure)** — library version skew, base-image
  drift, or a stale model on one cluster. This is what the drill parity test is for: fix
  the skew, do not explain it away.

### Monitoring / k6

- **Grafana dashboards empty** — check the datasource provisioning and that each
  provider's Prometheus is scraping its own targets; verify `/federate` is reachable over
  the tunnel from the control plane.
- **`lapse_api` target down** — its `metrics_path` is `/metrics` through nginx ingress;
  make sure the API service is exposed and the instrumentator endpoint responds.
- **k6 thresholds failing on one provider** — the spec budget is p95 < 1000 ms, < 1%
  errors. Check that provider's HPA scaling and CPU limits (`500m`) before blaming the
  test — and note it as a drill-relevant finding if the secondary is slower.
