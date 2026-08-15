output "vpc_id" {
  description = "ID of the VPC"
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

output "cp_public_ip" {
  description = "Public IP of the control plane VM"
  value       = module.cp.public_ip
}

output "cp_internal_ip" {
  description = "Internal IP of the control plane VM"
  value       = module.cp.internal_ip
}

output "w1_public_ip" {
  description = "Public IP of worker 1"
  value       = module.w1.public_ip
}

output "w1_internal_ip" {
  description = "Internal IP of worker 1"
  value       = module.w1.internal_ip
}

output "w2_public_ip" {
  description = "Public IP of worker 2"
  value       = module.w2.public_ip
}

output "w2_internal_ip" {
  description = "Internal IP of worker 2"
  value       = module.w2.internal_ip
}

output "worker_public_ips" {
  description = "Public IPs of all workers"
  value       = [module.w1.public_ip, module.w2.public_ip]
}
