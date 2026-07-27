# GitHub Actions Docker Kubernetes CI Pipeline

## Overview

This project demonstrates an end-to-end CI pipeline using GitHub Actions, Docker, Docker Hub, and Kubernetes (Minikube).

The application is a Flask web service that is containerized with Docker, automatically built and published to Docker Hub through GitHub Actions, and deployed to Kubernetes. Configuration is managed using ConfigMaps, while sensitive information is stored in Kubernetes Secrets.

---

## Architecture

```text
Developer
    │
    ▼
Git Push
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ├── Checkout Source Code
    ├── Install Dependencies
    ├── Validate Application
    ├── Build Docker Image
    ├── Push Image to Docker Hub
    │
    ▼
Docker Hub
    │
    ▼
Kubernetes Deployment
    │
    ▼
Pods
    │
    ├── ConfigMap
    └── Secret
    │
    ▼
Flask Application
```

---

## Technologies

- Python (Flask)
- Docker
- Docker Hub
- GitHub Actions
- Kubernetes (Minikube)
- ConfigMaps
- Secrets

---

## Project Structure

```text
github-actions-docker-project/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── configmap.yaml
│   └── secret.yaml
│
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## CI Pipeline

The GitHub Actions workflow performs the following tasks automatically whenever code is pushed to the `main` branch:

1. Checks out the repository.
2. Sets up the Python environment.
3. Installs project dependencies.
4. Validates the Flask application.
5. Builds the Docker image.
6. Pushes the image to Docker Hub using GitHub Secrets.

---

## Kubernetes Deployment

The application is deployed using Kubernetes resources:

- Deployment
- Service (NodePort)
- ConfigMap
- Secret

The Flask application reads:

| Environment Variable | Source |
|----------------------|--------|
| `APP_MESSAGE` | ConfigMap |
| `DB_PASSWORD` | Secret |

---

## Running the Project

### Build the Docker image

```bash
docker build -t github-actions-demo .
```

### Run locally

```bash
docker run -p 5000:5000 ^
-e APP_MESSAGE="Hello from Docker" ^
-e DB_PASSWORD="MyPassword123" ^
github-actions-demo
```

### Deploy to Kubernetes

```bash
kubectl apply -f k8s/
```

---

## Learning Outcomes

This project demonstrates practical experience with:

- Docker image creation and containerization
- GitHub Actions CI pipelines
- Docker Hub image publishing
- Kubernetes Deployments and Services
- ConfigMaps and Secrets
- Environment variable management
- Kubernetes troubleshooting (`CreateContainerConfigError`)
- Rolling updates using Deployments



