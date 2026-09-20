variable "docker_host" {
  description = "Docker daemon socket (local)."
  type        = string
  default     = "unix:///var/run/docker.sock"
}

variable "postgres_port" {
  description = "Host port for Postgres."
  type        = number
  default     = 5432
}

variable "mlflow_port" {
  description = "Host port for the MLflow tracking server."
  type        = number
  default     = 5000
}

variable "mlflow_image" {
  description = "Local MLflow image (build via docker/mlflow)."
  type        = string
  default     = "mlops-local-mlflow:latest"
}
