variable "project_id" {
  description = "GCP project ID"
  type        = string
}

variable "region" {
  description = "GCP region"
  type        = string
  default     = "europe-west1"
}

variable "zone" {
  description = "GCP zone"
  type        = string
  default     = "europe-west1-b"
}

variable "name_prefix" {
  description = "Prefix for all created resources"
  type        = string
  default     = "gcp"
}

variable "credentials_file" {
  description = "Path to the GCP service account JSON credentials file (empty = ADC)"
  type        = string
  default     = ""
}

variable "ssh_public_key" {
  description = "Public SSH key installed on all VMs (ubuntu user)"
  type        = string
}

variable "node_exporter_source_cidrs" {
  description = "CIDRs allowed to reach node exporter port 9100. Set to the public IP of the oci-monitoring VM, e.g. [\"1.2.3.4/32\"]"
  type        = list(string)
  default     = ["0.0.0.0/0"]
}
