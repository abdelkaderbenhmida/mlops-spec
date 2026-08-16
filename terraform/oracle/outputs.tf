output "vcn_id" {
  description = "ID of the VCN"
  value       = module.network.network_id
}

output "subnet_id" {
  description = "ID of the subnet"
  value       = module.network.subnet_id
}

output "subnet_cidr" {
  description = "CIDR block of the subnet"
  value       = module.network.subnet_cidr
}

output "training_public_ip" {
  description = "Public IP of the training VM (MLflow)"
  value       = module.training.public_ip
}

output "training_internal_ip" {
  description = "Internal IP of the training VM"
  value       = module.training.internal_ip
}

output "monitoring_public_ip" {
  description = "Public IP of the monitoring VM (Prometheus + Grafana)"
  value       = module.monitoring.public_ip
}

output "monitoring_internal_ip" {
  description = "Internal IP of the monitoring VM"
  value       = module.monitoring.internal_ip
}
