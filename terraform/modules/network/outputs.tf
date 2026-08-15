output "network_id" {
  description = "ID of the VPC (GCP) or VCN (OCI)"
  value       = var.cloud == "gcp" ? google_compute_network.vpc[0].id : oci_core_vcn.vcn[0].id
}

output "subnet_id" {
  description = "ID of the subnet"
  value       = var.cloud == "gcp" ? google_compute_subnetwork.subnet[0].id : oci_core_subnet.subnet[0].id
}

output "subnet_cidr" {
  description = "CIDR block of the subnet"
  value       = var.cloud == "gcp" ? google_compute_subnetwork.subnet[0].ip_cidr_range : oci_core_subnet.subnet[0].cidr_block
}
