terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
    oci = {
      source  = "oracle/oci"
      version = "~> 5.0"
    }
  }
}

locals {
  gcp = var.cloud == "gcp" ? 1 : 0
  oci = var.cloud == "oci" ? 1 : 0
}

# ---------------------------------------------------------------
# Images
# ---------------------------------------------------------------
data "google_compute_image" "ubuntu" {
  count   = local.gcp
  project = var.gcp_image_project
  family  = var.gcp_image_family
}

data "oci_identity_availability_domains" "ads" {
  count          = local.oci
  compartment_id = var.oci_compartment_id
}

data "oci_core_images" "ubuntu" {
  count                    = local.oci
  compartment_id           = var.oci_compartment_id
  operating_system         = "Canonical Ubuntu"
  operating_system_version = var.oci_image_version
  shape                    = var.oci_shape
  sort_by                  = "TIMECREATED"
  sort_order               = "DESC"
}

# ---------------------------------------------------------------
# GCP instance
# ---------------------------------------------------------------
resource "google_compute_instance" "vm" {
  count                     = local.gcp
  name                      = var.vm_name
  machine_type              = var.machine_type
  zone                      = var.zone
  project                   = var.gcp_project_id
  tags                      = var.tags
  allow_stopping_for_update = true

  boot_disk {
    initialize_params {
      image = data.google_compute_image.ubuntu[0].self_link
      size  = var.disk_size_gb
    }
  }

  network_interface {
    subnetwork = var.subnet_id
    network_ip = var.internal_ip
    access_config {}
  }

  metadata = {
    ssh-keys = "ubuntu:${var.ssh_public_key}"
  }

  metadata_startup_script = var.startup_script
}

# ---------------------------------------------------------------
# OCI instance
# ---------------------------------------------------------------
resource "oci_core_instance" "vm" {
  count               = local.oci
  compartment_id      = var.oci_compartment_id
  availability_domain = var.availability_domain != "" ? var.availability_domain : data.oci_identity_availability_domains.ads[0].availability_domains[0].name
  display_name        = var.vm_name
  shape               = var.oci_shape

  shape_config {
    ocpus         = var.oci_ocpus
    memory_in_gbs = var.oci_memory_gb
  }

  create_vnic_details {
    subnet_id        = var.subnet_id
    assign_public_ip = true
    private_ip       = var.internal_ip
    display_name     = "${var.vm_name}-vnic"
  }

  source_details {
    source_type = "image"
    source_id   = data.oci_core_images.ubuntu[0].images[0].id
  }

  metadata = {
    ssh_authorized_keys = var.ssh_public_key
  }
}
