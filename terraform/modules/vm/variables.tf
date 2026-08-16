variable "cloud" {
  description = "Cloud provider: gcp or oci"
  type        = string
  validation {
    condition     = contains(["gcp", "oci"], var.cloud)
    error_message = "cloud must be either 'gcp' or 'oci'."
  }
}

variable "name_prefix" {
  description = "Prefix for resource names"
  type        = string
}

variable "vm_name" {
  description = "Name of the VM instance"
  type        = string
}

variable "subnet_id" {
  description = "ID of the subnet to attach the VM to"
  type        = string
}

variable "internal_ip" {
  description = "Static internal/private IP address for the VM"
  type        = string
}

variable "ssh_public_key" {
  description = "Public SSH key installed on the VM (ubuntu user)"
  type        = string
}

variable "machine_type" {
  description = "GCP machine type (used when cloud=gcp)"
  type        = string
  default     = "e2-medium"
}

variable "zone" {
  description = "GCP zone (used when cloud=gcp)"
  type        = string
  default     = ""
}

variable "gcp_project_id" {
  description = "GCP project ID (used when cloud=gcp)"
  type        = string
  default     = ""
}

variable "gcp_image_project" {
  description = "GCP image project (used when cloud=gcp)"
  type        = string
  default     = "ubuntu-os-cloud"
}

variable "gcp_image_family" {
  description = "GCP image family (used when cloud=gcp)"
  type        = string
  default     = "ubuntu-2204-lts"
}

variable "disk_size_gb" {
  description = "Boot disk size in GB"
  type        = number
  default     = 20
}

variable "startup_script" {
  description = "Optional startup script for GCP instances"
  type        = string
  default     = ""
}

variable "tags" {
  description = "Network tags applied to GCP instances"
  type        = list(string)
  default     = []
}

variable "oci_compartment_id" {
  description = "OCI compartment OCID (used when cloud=oci)"
  type        = string
  default     = ""
}

variable "oci_shape" {
  description = "OCI instance shape (used when cloud=oci)"
  type        = string
  default     = "VM.Standard.E2.1.Micro"
}

variable "oci_image_version" {
  description = "OCI Canonical Ubuntu image version (used when cloud=oci)"
  type        = string
  default     = "22.04"
}

variable "oci_ocpus" {
  description = "Number of OCPUs for the OCI shape"
  type        = number
  default     = 1
}

variable "oci_memory_gb" {
  description = "Memory in GB for the OCI shape"
  type        = number
  default     = 1
}

variable "availability_domain" {
  description = "OCI availability domain name (auto-detected when empty)"
  type        = string
  default     = ""
}
