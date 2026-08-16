# Deployment Guide

End-to-end deployment of the Enterprise MLOps Platform for customer churn
prediction, following the order defined in
[`mlops-platform-spec.md` §Deployment Order](../mlops-platform-spec.md):

```
1. terraform apply (oracle/)   → OCI VMs up first (MLflow needed before API)
2. terraform apply (gcp/)      → GCP VMs created
3. ansible-playbook site.yml   → all servers configured, K8s initialized
4. python ml/train.py          → model trained, registered in MLflow
5. kubectl apply -f kubernetes/ → API + DB deployed
6. Jenkins configured (manual, first time only)
7. k6 run loadtest.js          → validate performance + HPA triggers
```

**Deploy OCI before GCP.** The API pods load their model from MLflow
(`http://<oci-training-ip>:5000`) at startup, so MLflow must exist first.

---

## Prerequisites

| Tool | Version | Used for |
|---|---|---|
| Terraform | >= 1.5 | provisioning `terraform/gcp`, `terraform/oracle` |
| Ansible | current | `ansible/playbooks/*.yml` |
| Python | 3.11 (recommended) | `ml/*` scripts |
| kubectl | 1.28 | cluster verification |
| k6 | current | load testing |

Credentials you must have ready:

- **GCP**: project ID, a service account with Compute permissions
  (or Application Default Credentials), a public SSH key for the `ubuntu` user.
- **OCI**: tenancy OCID, user OCID, API key fingerprint, API private key PEM
  path, compartment OCID, region, and the same public SSH key.
- The SSH key is used by Terraform to inject `ubuntu:<public_key>` on GCP and
  `ssh_authorized_keys` on OCI, and by Ansible to connect.

> All credentials are supplied via variables/env — never commit them to the repo.

---

## 1. Provision OCI VMs (first)

Terraform state is separate per provider. Create the OCI environment first.

```bash
cd terraform/oracle
terraform init
```

Create `terraform.tfvars` (edit the placeholders):

```hcl
tenancy_ocid     = "ocid1.tenancy.oc1..xxxx"
user_ocid        = "ocid1.user.oc1..xxxx"
fingerprint      = "aa:bb:cc:dd:ee:ff:00:11"
private_key_path = "~/.oci/oci_api_key.pem"
compartment_id   = "ocid1.compartment.oc1..xxxx"
region           = "eu-frankfurt-1"
ssh_public_key   = "ssh-ed25519 AAAA… your-comment"
# optional: name_prefix = "oci"
```

Apply:

```bash
terraform apply
```

This creates the VCN + subnet `10.0.2.0/24`, the security list (ingress
`22, 5000, 9090, 3000`), and the VMs `oci-training` (`10.0.2.10`) and
`oci-monitoring` (`10.0.2.11`).

Capture the outputs:

```bash
terraform output
# training_public_ip     → public IP of the MLflow server
# monitoring_public_ip   → public IP of Prometheus/Grafana
```

## 2. Provision GCP VMs (second)

```bash
cd ../gcp
terraform init
```

Create `terraform.tfvars`:

```hcl
project_id     = "my-mlops-project"
region         = "europe-west1"
zone           = "europe-west1-b"
ssh_public_key = "ssh-ed25519 AAAA… your-comment"

# Restrict node exporter scraping to the oci-monitoring VM (IP allowlisting).
# Replace with the public IP from step 1, e.g. ["129.0.0.11/32"].
node_exporter_source_cidrs = ["0.0.0.0/0"]

# Optional: point to a service-account JSON; otherwise ADC is used.
# credentials_file = "~/.gcp/mlops-sa.json"
```

> **Security note:** `node_exporter_source_cidrs` defaults to `0.0.0.0/0` so the
> apply completes with zero manual steps. Set it to the **public IP of
> `oci-monitoring`** (as a `/32`) as soon as you know it, and re-apply.

Apply:

```bash
terraform apply
```

This creates the VPC + subnet `10.0.1.0/24`, the firewall rules
(`22, 80, 443, 6443, 30000–32767, 9100`), and the three VMs `gcp-k8s-cp`
(`10.0.1.10`), `gcp-k8s-w1` (`10.0.1.11`), `gcp-k8s-w2` (`10.0.1.12`).

```bash
terraform output   # cp_public_ip, w1/w2_public_ip, worker_public_ips, ...
```

**Verify:** all five VMs are up and reachable over SSH as `ubuntu`.

---

## 3. Configure all servers with Ansible

The Ansible inventory (`ansible/inventory/hosts.yml`) is a **static fallback**
containing placeholder IPs (`35.0.0.10`, `129.0.0.10`, …). Replace
`ansible_host` with the real public IPs from the Terraform outputs before
running (the dynamic inventory normally comes from Terraform outputs).

Then run the master playbook:

```bash
cd ansible
ansible-playbook -i inventory/hosts.yml playbooks/site.yml
```

The master playbook runs, in order:

1. **all hosts**: `common` (timezone, base packages, node exporter, UFW) + `docker` (Docker CE).
2. **gcp_k8s**: `kubernetes` — swap off, kubeadm 1.28, `kubeadm init --pod-network-cidr=192.168.0.0/16` on the CP, Calico CNI, workers joined, all nodes waited for `Ready`.
3. **oci-training**: `mlflow` (MLflow + PostgreSQL containers) and `training` (Python 3.11 venv, deps, scripts, `MLFLOW_TRACKING_URI`).
4. **oci-monitoring**: `monitoring` (Prometheus + Grafana containers + provisioning).

Targeted playbooks are also available:

```bash
ansible-playbook -i inventory/hosts.yml playbooks/k8s.yml        # cluster only
ansible-playbook -i inventory/hosts.yml playbooks/ml.yml         # training + MLflow
ansible-playbook -i inventory/hosts.yml playbooks/monitoring.yml # Prometheus + Grafana
```

**Verify:**

```bash
ssh ubuntu@<gcp-cp-ip> "kubectl get nodes -o wide"     # 3 nodes Ready
curl http://<oci-training-ip>:5000/health              # MLflow is alive
curl http://<oci-monitoring-ip>:9090/-/healthy         # Prometheus is alive
curl -u admin:admin http://<oci-monitoring-ip>:3000/api/health   # Grafana
```

The MLflow URL your API will use is `http://<oci-training-public-ip>:5000`
(pods reach it over the public IP — see the networking section of
[`architecture.md`](architecture.md)).

---

## 4. Train and register the model

Run training on `oci-training` (the `training` role prepared `/opt/ml` and the
venv, and set `MLFLOW_TRACKING_URI`):

```bash
ssh ubuntu@<oci-training-ip>
cd /opt/ml
/opt/ml-env/bin/python train.py
```

Locally (from the repo root, with MLflow reachable):

```bash
export MLFLOW_TRACKING_URI="http://<oci-training-public-ip>:5000"
python ml/train.py
```

`train.py` logs params/metrics (accuracy, f1, roc_auc), registers the model as
**`churn-model`** in the MLflow Model Registry, and saves `ml/model.pkl`.

**Verify:** open `http://<oci-training-ip>:5000`, confirm the run under
experiment `customer-churn` and the registered model `churn-model` version 1.

Run the CI gate locally to confirm it passes:

```bash
export MLFLOW_TRACKING_URI="http://<oci-training-public-ip>:5000"
python ml/evaluate.py      # exits 0 if accuracy >= 0.75, else 1
```

---

## 5. Deploy the API and database to Kubernetes

From `gcp-k8s-cp` (kubeconfig is at `/home/ubuntu/.kube/config`):

```bash
ssh ubuntu@<gcp-cp-ip>
kubectl apply -f kubernetes/
```

`kubernetes/` currently contains `namespace.yaml` (namespace `mlops`) and
`api/deployment.yaml` (Deployment `churn-api`, 2 replicas). Per the spec the
remaining manifests — `api/service.yaml`, `api/hpa.yaml`, `api/ingress.yaml`,
`configmap.yaml` (`MLFLOW_TRACKING_URI`, `DB_HOST`), and the PostgreSQL
StatefulSet + PVC + Secret — join `kubernetes/` and are applied by the same
command. The Deployment already references the ConfigMap `mlops-config` and
Secret `postgres-secret`.

Set `MLFLOW_TRACKING_URI` in the ConfigMap to `http://<oci-training-public-ip>:5000`.

**Verify:**

```bash
kubectl -n mlops get pods          # 2x churn-api Running/Ready
kubectl -n mlops get deploy,svc,hpa,pvc
curl http://<gcp-lb-or-nodeport>/health        # {"status":"ok","model_version":"1"}
```

Exercise the API:

```bash
curl -X POST http://<gcp-lb-or-nodeport>/predict \
  -H "Content-Type: application/json" \
  -d '{"tenure":12,"monthly_charges":65.5,"total_charges":786.0,
       "contract":"Month-to-month","payment_method":"Electronic check"}'
# {"prediction":0|1,"probability":0.87}

curl "http://<gcp-lb-or-nodeport>/predictions?limit=5"   # rows from PostgreSQL
```

---

## 6. Jenkins first-time setup (manual)

Jenkins runs as a Docker container **on `gcp-k8s-cp`** and is triggered on push
to `main`. First-time, manual setup:

1. Start the Jenkins container on `gcp-k8s-cp` (Docker is already installed by
   the `docker` role).
2. Unlock Jenkins with the initial admin password from the container logs.
3. Add credentials to the Jenkins credential store:
   - **Docker Hub** credentials (for `docker build`/`docker push`),
   - **kubeconfig** as a secret file (from `/home/ubuntu/.kube/config`),
   - **OCI SSH key** as an SSH credential (for the `ssh oci-training` train step).
4. Create a pipeline job pointing at the repo's `Jenkinsfile`, with a webhook
   so a push to `main` triggers the pipeline.

Pipeline stages (per spec): Checkout → Test (`pytest api/` + `python
ml/evaluate.py`) → Train (`ssh oci-training: python ml/train.py`) → Build
(`docker build -t <registry>/churn-api:$BUILD_NUMBER`) → Push → Deploy
(`kubectl set image deployment/churn-api …`). The build **fails** if
`evaluate.py` exits 1 (accuracy < 0.75).

---

## 7. Load test with k6

Per the spec, run k6 **from `oci-monitoring`** against the GCP API external IP /
ingress:

```bash
ssh ubuntu@<oci-monitoring-ip>
k6 run /path/to/monitoring/k6/loadtest.js --env API_URL=http://<gcp-lb-ip>:80
```

The test (spec): 20 virtual users for 2 minutes, 70% `GET /health`, 30%
`POST /predict`, with thresholds `http_req_duration p(95) < 1000ms` and
`http_req_failed < 1%`. Watch Grafana (ML API dashboard) and HPA behavior while
it runs.

**Verify:**

```bash
kubectl -n mlops get hpa          # CPU utilization climbing; replicas 2 → up to 8
```

---

## Acceptance checkpoints

| Check | Command |
|---|---|
| 5 VMs provisioned | `terraform output` in both provider dirs |
| Cluster healthy | `kubectl get nodes` → 3 nodes `Ready` |
| Model registered | MLflow UI at `http://<oci-training-ip>:5000` → `churn-model` |
| Predictions work | `curl POST /predict` and `GET /predictions` |
| Monitoring live | Grafana `http://<oci-monitoring-ip>:3000` shows node + API + ML dashboards |
| HPA scales | `kubectl -n mlops get hpa` during k6 |
| CI green | Jenkins pipeline on push to `main` |
| k6 within budget | p95 < 1000 ms, error rate < 1% |
| No hardcoded secrets | `rg -i "password\|secret" --glob '!*.md'` → env/secret references only |

---

## Troubleshooting

### Terraform

- **`terraform apply` hangs creating OCI instances** — OCI `VM.Standard.E2.1.Micro`
  availability varies by AD/region. Set `availability_domain` in the VM module
  call if the auto-detected first AD is full.
- **Provider credentials rejected** — confirm OCI `fingerprint`/`private_key_path`
  match the API key uploaded to the user, and that the GCP service account has
  `compute.instances.create` permissions. GCP falls back to Application Default
  Credentials when `credentials_file` is empty.
- **Firewall changes not applied** — re-run `terraform apply` after changing
  `node_exporter_source_cidrs`; GCP firewall rules update in place.

### Ansible

- **`ansible-playbook site.yml` fails to connect** — `ansible/inventory/hosts.yml`
  is a static fallback with placeholder IPs; replace `ansible_host` values with
  the real public IPs from `terraform output`, and confirm the SSH key path
  (`ansible_ssh_private_key_file`) matches.
- **Re-run safety** — all roles are idempotent; re-running the playbook is safe.
- **kubeadm init needs a working kubelet** — the role disables swap, loads
  `overlay`/`br_netfilter`, and configures containerd's systemd cgroup driver
  before init; if init fails on cgroup errors, check `docker info` for
  `cgroup driver` = systemd on every node.
- **Worker join fails** — the join command is generated on the CP with
  `kubeadm token create --print-join-command`; ensure port 6443 is reachable
  from workers (GCP firewall `gcp-allow-k8s-api`).
- **node exporter not scraped** — node exporter is installed by `common` on
  every host and listens on `:9100`. From `oci-monitoring` run
  `curl http://<gcp-cp-ip>:9100/metrics`. If it times out, the GCP
  `node_exporter_source_cidrs` rule excludes the monitoring VM's IP.
- **MLflow not reachable from the API pods** — confirm the OCI security list
  allows port 5000 (`oci_security_list_ports = [22, 5000, 9090, 3000]`), MLflow
  binds `0.0.0.0` (`mlflow_host` default), and the ConfigMap
  `MLFLOW_TRACKING_URI` points at the **public** IP of `oci-training`.

### ML / API

- **`train.py` can't find the CSV** — it defaults to `ml/data/churn.csv`
  relative to the working directory; on `oci-training` run from `/opt/ml` (data
  is copied to `/opt/ml/data/churn.csv`). Override with `CHURN_DATA_PATH`.
- **`evaluate.py` exits 1** — accuracy below the 0.75 gate; retrain or accept
  the lower model. The gate is intentional CI behavior.
- **API pods crash-looping at startup** — the app fails if MLflow is
  unreachable (`load_model()` raises) or PostgreSQL isn't up. Deploy the
  database manifests first and confirm `MLFLOW_TRACKING_URI` resolves.
- **HPA never scales** — CPU-based autoscaling requires the Kubernetes
  **metrics-server**; install it in the cluster if it is absent, then re-check
  `kubectl -n mlops get hpa`.

### Monitoring / k6

- **Grafana dashboards empty** — check the datasource provisioning
  (`/opt/grafana/provisioning`) and that Prometheus is scraping
  (`Status → Targets` in the Prometheus UI). The custom dashboard file lives at
  `/opt/grafana/dashboards/ml-api-dashboard.json`.
- **`churn_api` target down** — its `metrics_path` is `/metrics` and it targets
  the GCP ingress `:80`; make sure the API service is exposed and the
  `prometheus-fastapi-instrumentator` `/metrics` endpoint responds.
- **k6 thresholds failing** — the spec budget is p95 < 1000 ms, < 1% errors.
  Check HPA scaling and API CPU limits (`500m`) before blaming the test.
