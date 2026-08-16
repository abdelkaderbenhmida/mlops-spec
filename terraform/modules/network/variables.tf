variable "cloud" {
  description = "Cloud provider: gcp or oci"
  type        = string
  validation {
    condition     = contains(["gcp", "oci"], var.cloud)
    error_message = "cloud must be either 'gcp' or 'oci'."
  }
}

variable "name_prefix" {
  description = "Prefix for all created resources"
  type        = string
}

variable "cidr_block" {
  description = "CIDR block for the network/subnet"
  type        = string
}

variable "region" {
  description = "GCP region (used when cloud=gcp)"
  type        = string
  default     = ""
}

variable "gcp_project_id" {
  description = "GCP project ID (used when cloud=gcp)"
  type        = string
  default     = ""
}

variable "oci_compartment_id" {
  description = "OCI compartment OCID (used when cloud=oci)"
  type        = string
  default     = ""
}

variable "node_exporter_source_cidrs" {
  description = "CIDRs allowed to reach node exporter port 9100 (GCP firewall)"
  type        = list(string)
  default     = []
}

variable "oci_security_list_ports" {
  description = "TCP ports allowed in the OCI security list ingress rules"
  type        = list(number)
  default     = [22, 5000, 9090, 3000]
}
