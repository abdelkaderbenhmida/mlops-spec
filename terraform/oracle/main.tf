terraform {
  required_version = ">= 1.5"

  required_providers {
    oci = {
      source  = "oracle/oci"
      version = "~> 5.0"
    }
  }
}

provider "oci" {
  tenancy_ocid     = var.tenancy_ocid
  user_ocid        = var.user_ocid
  fingerprint      = var.fingerprint
  private_key_path = var.private_key_path
  region           = var.region
}

module "network" {
  source      = "../modules/network"
  cloud       = "oci"
  name_prefix = var.name_prefix

  cidr_block         = "10.0.2.0/24"
  oci_compartment_id = var.compartment_id

  oci_security_list_ports = [22, 5000, 9090, 3000]
}

locals {
  static_ips = {
    training   = "10.0.2.10"
    monitoring = "10.0.2.11"
  }
}

module "training" {
  source      = "../modules/vm"
  cloud       = "oci"
  name_prefix = var.name_prefix
  vm_name     = "oci-training"
  oci_shape   = "VM.Standard.E2.1.Micro"

  oci_compartment_id = var.compartment_id

  subnet_id      = module.network.subnet_id
  internal_ip    = local.static_ips.training
  ssh_public_key = var.ssh_public_key
}

module "monitoring" {
  source      = "../modules/vm"
  cloud       = "oci"
  name_prefix = var.name_prefix
  vm_name     = "oci-monitoring"
  oci_shape   = "VM.Standard.E2.1.Micro"

  oci_compartment_id = var.compartment_id

  subnet_id      = module.network.subnet_id
  internal_ip    = local.static_ips.monitoring
  ssh_public_key = var.ssh_public_key
}
