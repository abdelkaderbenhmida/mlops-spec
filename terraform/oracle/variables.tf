variable "tenancy_ocid" {
  description = "OCI tenancy OCID"
  type        = string
}

variable "user_ocid" {
  description = "OCI user OCID"
  type        = string
}

variable "fingerprint" {
  description = "OCI API key fingerprint"
  type        = string
}

variable "private_key_path" {
  description = "Path to the OCI API private key PEM file"
  type        = string
}

variable "compartment_id" {
  description = "OCI compartment OCID"
  type        = string
}

variable "region" {
  description = "OCI region"
  type        = string
}

variable "name_prefix" {
  description = "Prefix for created resources"
  type        = string
  default     = "oci"
}

variable "ssh_public_key" {
  description = "Public SSH key installed on all VMs (ubuntu user)"
  type        = string
}
