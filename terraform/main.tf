terraform {
  required_version = ">= 1.5"

  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

# ALL-LOCAL: Infrastructure is provisioned on the local Docker daemon.
# No cloud provider, no credentials, no remote state.

provider "docker" {
  host = var.docker_host
}

resource "docker_network" "mlops" {
  name = "mlops-local-net"
}

resource "docker_volume" "pg_data" {
  name = "mlops-local-pg-data"
}

resource "docker_volume" "mlflow_artifacts" {
  name = "mlops-local-mlflow-artifacts"
}

resource "docker_container" "postgres" {
  name  = "mlops-local-postgres"
  image = "postgres:16"

  networks_advanced {
    name = docker_network.mlops.name
  }

  env = [
    "POSTGRES_USER=mlops",
    "POSTGRES_PASSWORD=mlops",
    "POSTGRES_DB=mlops",
  ]

  ports {
    internal = 5432
    external = var.postgres_port
  }

  volumes {
    volume_name    = docker_volume.pg_data.name
    container_path = "/var/lib/postgresql/data"
  }

  healthcheck {
    test     = ["CMD-SHELL", "pg_isready -U mlops -d mlops"]
    interval = "10s"
    timeout  = "5s"
    retries  = 5
  }

  restart = "unless-stopped"
}

resource "docker_container" "mlflow" {
  name  = "mlops-local-mlflow"
  image = var.mlflow_image

  networks_advanced {
    name = docker_network.mlops.name
  }

  command = [
    "--host", "0.0.0.0",
    "--port", "5000",
    "--backend-store-uri", "postgresql://mlops:mlops@postgres:5432/mlops",
    "--default-artifact-root", "file:///opt/mlflow/artifacts",
  ]

  ports {
    internal = 5000
    external = var.mlflow_port
  }

  volumes {
    volume_name    = docker_volume.mlflow_artifacts.name
    container_path = "/opt/mlflow/artifacts"
  }

  depends_on = [docker_container.postgres]
  restart    = "unless-stopped"
}
