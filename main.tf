# main.tf

# 1. Configure the Docker provider
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

# 2. Create a private network for the containers to communicate
resource "docker_network" "app_network" {
  name = "auth-app-network"
}

# 3. Pull the backend image from Docker Hub
resource "docker_image" "backend_image" {
  name = "azamdevops/auth-backend:latest"
}

# 4. Pull the frontend image from Docker Hub
resource "docker_image" "frontend_image" {
  name = "azamdevops/auth-frontend:latest"
}

# 5. Create the backend container
resource "docker_container" "backend_container" {
  name  = "prod-auth-backend"
  image = docker_image.backend_image.image_id
  networks_advanced {
    name = docker_network.app_network.name
  }
  # This makes your database data persistent
  volumes {
    host_path      = "${path.cwd}/backend/database.db"
    container_path = "/app/database.db"
  }
  # This maps the container's port 5000 to your machine's port 5000
  ports {
    internal = 5000
    external = 5000
  }
}

# 6. Create the frontend container
resource "docker_container" "frontend_container" {
  name  = "prod-auth-frontend"
  image = docker_image.frontend_image.image_id
  networks_advanced {
    name = docker_network.app_network.name
  }
  # This maps the container's port 3000 to your machine's port 3000
  ports {
    internal = 3000
    external = 3000
  }
  # This ensures the backend container starts before the frontend
  depends_on = [docker_container.backend_container]
}