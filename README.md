# GitHub Actions Docker Kubernetes Project

This project demonstrates an end-to-end DevOps workflow.

## Technologies Used

- Python Flask
- Docker
- Kubernetes
- GitHub Actions
- Docker Hub

## Project Flow

Code Push
   |
   v
GitHub Repository
   |
   v
GitHub Actions CI Pipeline
   |
   v
Docker Image Build
   |
   v
Docker Hub
   |
   v
Kubernetes Deployment

## Kubernetes Features

- Deployment
- Service
- ConfigMap
- Secret

## Application Configuration

The Flask application reads:

- APP_MESSAGE from Kubernetes ConfigMap
- DB_PASSWORD from Kubernetes Secret