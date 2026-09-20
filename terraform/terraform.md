# Terraform — ALL-LOCAL

Ferry provisions its infrastructure **locally only**. There is no cloud
provider, no credentials, and no remote state. Terraform manages the local
Docker resources (network, volumes, Postgres, MLflow) via the
`kreuzwerker/docker` provider.

## Usage

```bash
cd terraform
terraform init
terraform plan
terraform apply
```

Outputs give the local MLflow tracking URI (`http://localhost:5000`) and the
local Postgres DSN.

## What was removed

- `terraform/gcp/` and `terraform/oracle/` (multi-cloud DORA variant) — removed.
- `terraform/modules/{network,vm}` (cloud VPC/VM modules) — removed.

## Validation (no apply required)

```bash
terraform init -backend=false
terraform validate
```
