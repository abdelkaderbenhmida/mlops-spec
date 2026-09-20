output "mlflow_tracking_uri" {
  description = "MLflow tracking URI exposed on the host."
  value       = "http://localhost:${var.mlflow_port}"
}

output "postgres_dsn" {
  description = "Postgres connection string (host side)."
  value       = "postgresql://mlops:mlops@localhost:${var.postgres_port}/mlops"
}

output "network_name" {
  value = docker_network.mlops.name
}
