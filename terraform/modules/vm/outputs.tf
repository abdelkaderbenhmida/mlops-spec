output "id" {
  description = "ID of the VM instance"
  value = var.cloud == "gcp"
    ? google_compute_instance.vm[0].id
    : oci_core_instance.vm[0].id
}

output "name" {
  description = "Name of the VM instance"
  value = var.cloud == "gcp"
    ? google_compute_instance.vm[0].name
    : oci_core_instance.vm[0].display_name
}

output "public_ip" {
  description = "Public IP address of the VM"
  value = var.cloud == "gcp"
    ? google_compute_instance.vm[0].network_interface[0].access_config[0].nat_ip
    : oci_core_instance.vm[0].public_ip
}

output "internal_ip" {
  description = "Static internal IP address of the VM"
  value = var.cloud == "gcp"
    ? google_compute_instance.vm[0].network_interface[0].network_ip
    : oci_core_instance.vm[0].private_ip
}
