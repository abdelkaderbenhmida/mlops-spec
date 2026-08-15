locals {
  gcp = var.cloud == "gcp" ? 1 : 0
  oci = var.cloud == "oci" ? 1 : 0
}

# ---------------------------------------------------------------
# GCP network
# ---------------------------------------------------------------
resource "google_compute_network" "vpc" {
  count                   = local.gcp
  name                    = "${var.name_prefix}-vpc"
  project                 = var.gcp_project_id
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "subnet" {
  count         = local.gcp
  name          = "${var.name_prefix}-subnet"
  project       = var.gcp_project_id
  region        = var.region
  network       = google_compute_network.vpc[0].id
  ip_cidr_range = var.cidr_block
  private_ip_google_access = true
}

resource "google_compute_firewall" "allow_ssh" {
  count       = local.gcp
  name        = "${var.name_prefix}-allow-ssh"
  network     = google_compute_network.vpc[0].name
  project     = var.gcp_project_id
  allow {
    protocol = "tcp"
    ports    = ["22"]
  }
  source_ranges = ["0.0.0.0/0"]
}

resource "google_compute_firewall" "allow_http" {
  count       = local.gcp
  name        = "${var.name_prefix}-allow-http"
  network     = google_compute_network.vpc[0].name
  project     = var.gcp_project_id
  allow {
    protocol = "tcp"
    ports    = ["80"]
  }
  source_ranges = ["0.0.0.0/0"]
}

resource "google_compute_firewall" "allow_https" {
  count       = local.gcp
  name        = "${var.name_prefix}-allow-https"
  network     = google_compute_network.vpc[0].name
  project     = var.gcp_project_id
  allow {
    protocol = "tcp"
    ports    = ["443"]
  }
  source_ranges = ["0.0.0.0/0"]
}

resource "google_compute_firewall" "allow_k8s_api" {
  count       = local.gcp
  name        = "${var.name_prefix}-allow-k8s-api"
  network     = google_compute_network.vpc[0].name
  project     = var.gcp_project_id
  allow {
    protocol = "tcp"
    ports    = ["6443"]
  }
  source_ranges = ["0.0.0.0/0"]
}

resource "google_compute_firewall" "allow_nodeports" {
  count       = local.gcp
  name        = "${var.name_prefix}-allow-nodeports"
  network     = google_compute_network.vpc[0].name
  project     = var.gcp_project_id
  allow {
    protocol = "tcp"
    ports    = ["30000-32767"]
  }
  source_ranges = ["0.0.0.0/0"]
}

resource "google_compute_firewall" "allow_node_exporter" {
  count         = local.gcp
  name          = "${var.name_prefix}-allow-node-exporter"
  network       = google_compute_network.vpc[0].name
  project       = var.gcp_project_id
  allow {
    protocol = "tcp"
    ports    = ["9100"]
  }
  source_ranges = var.node_exporter_source_cidrs
}

# ---------------------------------------------------------------
# OCI network
# ---------------------------------------------------------------
resource "oci_core_vcn" "vcn" {
  count          = local.oci
  compartment_id = var.oci_compartment_id
  cidr_blocks    = [var.cidr_block]
  display_name   = "${var.name_prefix}-vcn"
  dns_label      = replace(var.name_prefix, "-", "")
}

resource "oci_core_internet_gateway" "igw" {
  count          = local.oci
  compartment_id = var.oci_compartment_id
  vcn_id         = oci_core_vcn.vcn[0].id
  display_name   = "${var.name_prefix}-igw"
  enabled        = true
}

resource "oci_core_route_table" "rt" {
  count          = local.oci
  compartment_id = var.oci_compartment_id
  vcn_id         = oci_core_vcn.vcn[0].id
  display_name   = "${var.name_prefix}-rt"
  route_rules {
    destination       = "0.0.0.0/0"
    destination_type  = "CIDR_BLOCK"
    network_entity_id = oci_core_internet_gateway.igw[0].id
  }
}

resource "oci_core_security_list" "sl" {
  count          = local.oci
  compartment_id = var.oci_compartment_id
  vcn_id         = oci_core_vcn.vcn[0].id
  display_name   = "${var.name_prefix}-security-list"

  egress_security_rules {
    destination = "0.0.0.0/0"
    protocol    = "all"
  }

  dynamic "ingress_security_rules" {
    for_each = var.oci_security_list_ports
    content {
      protocol = "6"
      source   = "0.0.0.0/0"
      tcp_options {
        destination_port_range {
          min = ingress_security_rules.value
          max = ingress_security_rules.value
        }
      }
    }
  }
}

resource "oci_core_subnet" "subnet" {
  count                = local.oci
  compartment_id       = var.oci_compartment_id
  vcn_id               = oci_core_vcn.vcn[0].id
  cidr_block           = var.cidr_block
  display_name         = "${var.name_prefix}-subnet"
  dns_label            = "sub${replace(var.name_prefix, "-", "")}"
  route_table_id       = oci_core_route_table.rt[0].id
  security_list_ids    = [oci_core_security_list.sl[0].id]
  prohibit_public_ip_on_vnic = false
}
