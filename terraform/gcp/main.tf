terraform {
  required_version = ">= 1.5"

  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project     = var.project_id
  region      = var.region
  zone        = var.zone
  credentials = var.credentials_file != "" ? file(var.credentials_file) : null
}

module "network" {
  source  = "../modules/network"
  cloud   = "gcp"
  name_prefix = var.name_prefix

  cidr_block     = "10.0.1.0/24"
  region         = var.region
  gcp_project_id = var.project_id

  # Restrict node exporter (9100) to the public IP of the oci-monitoring VM.
  # Defaults to 0.0.0.0/0 for zero-manual-step applies — restrict before
  # exposing the cluster to the internet.
  node_exporter_source_cidrs = var.node_exporter_source_cidrs
}

locals {
  static_ips = {
    cp = "10.0.1.10"
    w1 = "10.0.1.11"
    w2 = "10.0.1.12"
  }
}

module "cp" {
  source       = "../modules/vm"
  cloud        = "gcp"
  name_prefix  = var.name_prefix
  vm_name      = "${var.name_prefix}-k8s-cp"
  machine_type = "e2-medium"
  zone         = var.zone
  gcp_project_id = var.project_id

  subnet_id    = module.network.subnet_id
  internal_ip  = local.static_ips.cp
  ssh_public_key = var.ssh_public_key
  tags         = ["k8s", "control-plane"]
}

module "w1" {
  source       = "../modules/vm"
  cloud        = "gcp"
  name_prefix  = var.name_prefix
  vm_name      = "${var.name_prefix}-k8s-w1"
  machine_type = "e2-medium"
  zone         = var.zone
  gcp_project_id = var.project_id

  subnet_id    = module.network.subnet_id
  internal_ip  = local.static_ips.w1
  ssh_public_key = var.ssh_public_key
  tags         = ["k8s", "worker"]
}

module "w2" {
  source       = "../modules/vm"
  cloud        = "gcp"
  name_prefix  = var.name_prefix
  vm_name      = "${var.name_prefix}-k8s-w2"
  machine_type = "e2-medium"
  zone         = var.zone
  gcp_project_id = var.project_id

  subnet_id    = module.network.subnet_id
  internal_ip  = local.static_ips.w2
  ssh_public_key = var.ssh_public_key
  tags         = ["k8s", "worker"]
}
