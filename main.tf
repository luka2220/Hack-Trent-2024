# Define the required provider
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.0"  # Specify the version you need
    }
  }
}

# Specify the Docker provider
provider "docker" {}

# Define the Docker network (same as your Docker Compose)
resource "docker_network" "app_network" {
  name   = "app_network"
  driver = "bridge"
}

# Build the Docker image from the Dockerfile
resource "docker_image" "backend_image" {
  name = "backend_image"
  build {
    context    = "."
    dockerfile = "docker/dockerfiles/Dockerfile"
  }
}

# Define the Docker container for the backend service
resource "docker_container" "backend" {
  name  = "backend"
  image = docker_image.backend_image.name  # Use the image name directly

  # Set environment variables using 'env' instead of 'environment'
  env = [
    "FLASK_APP=main.py",
    "FLASK_ENV=development",
    "DATABASE_URL=sqlite:////app/db/hacktrent.db"
  ]

  # Connect the container to the app_network
  networks_advanced {
    name = docker_network.app_network.name
  }

  # Define port mappings (host -> container)
  ports {
    internal = 8000
    external = 8001
  }
}
