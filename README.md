# Production Reliability Platform

A production-style DevOps and DevSecOps platform demonstrating automated CI/CD, containerization, Kubernetes deployment, infrastructure validation, security scanning, and application observability.

## Architecture

Developer

  |

  v

GitHub

  |

  v

GitHub Actions

  |

  +-- Python Tests

  +-- Terraform Validation

  +-- Kubernetes Validation

  +-- Gitleaks Secret Scan

  +-- pip-audit Dependency Scan

  +-- Docker Build

  +-- Trivy Container Scan

  |

  v

GitHub Container Registry

  |

  v

Kubernetes / Minikube

  |

  +-- Replica 1

  +-- Replica 2

  |

  v

Prometheus

  |

  v

Grafana

## Key Features

- FastAPI production-style application

- Docker containerization

- Kubernetes deployment with 2 replicas

- Readiness and liveness probes

- Kubernetes self-healing

- Resource requests and limits

- Terraform infrastructure configuration

- GitHub Actions CI/CD

- GitHub Container Registry

- Gitleaks secret scanning

- pip-audit Python dependency scanning

- Trivy container vulnerability scanning

- Prometheus metrics collection

- Grafana monitoring dashboard

- Persistent Grafana storage

- Kubernetes manifest validation with Kubeconform

## Tech Stack

| Category | Technology |

|---|---|

| Application | Python, FastAPI |

| Containerization | Docker |

| Orchestration | Kubernetes, Minikube |

| CI/CD | GitHub Actions |

| Registry | GitHub Container Registry |

| Infrastructure | Terraform |

| Security | Gitleaks, pip-audit, Trivy |

| Monitoring | Prometheus, Grafana |

| Validation | Kubeconform |

| Version Control | Git, GitHub |

## Project Structure

devops-production-platform/

├── app/

│   └── main.py

├── infrastructure/

│   ├── kubernetes/

│   │   ├── deployment.yaml

│   │   └── service.yaml

│   ├── monitoring/

│   │   ├── grafana-deployment.yaml

│   │   ├── grafana-pvc.yaml

│   │   ├── grafana-service.yaml

│   │   ├── prometheus-config.yaml

│   │   ├── prometheus-deployment.yaml

│   │   └── prometheus-service.yaml

│   └── terraform/

│       ├── main.tf

│       ├── variables.tf

│       ├── outputs.tf

│       └── versions.tf

├── .github/

│   └── workflows/

│       └── ci.yml

├── Dockerfile

├── requirements.txt

├── .gitignore

└── README.md

## Application

The application is built with FastAPI and exposes the following endpoints:

| Endpoint | Purpose |

|---|---|

| `/` | Application information |

| `/health` | Health check |

| `/api/info` | Application metadata |

| `/metrics` | Prometheus metrics |

## Local Development

Create a virtual environment:

    python3 -m venv .venv

Activate it:

    source .venv/bin/activate

Install dependencies:

    pip install -r requirements.txt

Run tests:

    pytest

Run the application:

    uvicorn app.main:app --reload

The application runs on:

    http://localhost:8000

Health endpoint:

    http://localhost:8000/health

Metrics endpoint:

    http://localhost:8000/metrics

## Docker

Build the image:

    docker build -t production-reliability-api:latest .

Run the container:

    docker run --rm -p 8000:8000 production-reliability-api:latest

Test the application:

    curl http://localhost:8000/health

## Terraform

Initialize Terraform:

    cd infrastructure/terraform

    terraform init

Format Terraform files:

    terraform fmt

Validate Terraform:

    terraform validate

Create a plan:

    terraform plan

Apply the configuration:

    terraform apply

## Kubernetes

Start Minikube:

    minikube start --driver=docker

Verify the cluster:

    kubectl get nodes

Build the application image:

    docker build -t production-reliability-api:latest .

Load the image into Minikube:

    minikube image load production-reliability-api:latest

Deploy the application:

    kubectl apply -f infrastructure/kubernetes/

Check the pods:

    kubectl get pods

Check the service:

    kubectl get svc

Access the application:

    minikube service production-reliability-api --url

## Kubernetes Reliability

The application runs with two replicas.

The deployment includes:

- Readiness probe

- Liveness probe

- CPU requests

- Memory requests

- CPU limits

- Memory limits

- Automatic pod recreation

### Self-Healing

The Kubernetes deployment was tested by deleting both application pods:

    kubectl delete pod -l app=production-reliability-api

Kubernetes automatically recreated both pods and returned them to:

    1/1 Running

This demonstrates Kubernetes self-healing and replica management.

## CI/CD Pipeline

GitHub Actions runs automatically on pushes to `main` and pull requests targeting `main`.

Pipeline stages:

    Checkout

      |

      v

    Gitleaks

      |

      v

    Python Dependency Installation

      |

      v

    Pytest

      |

      v

    Terraform Validation

      |

      v

    Kubernetes Validation

      |

      v

    Monitoring Validation

      |

      v

    Docker Build

      |

      v

    Trivy Security Scan

      |

      v

    Push Image to GHCR

## DevSecOps

Security is integrated directly into the CI/CD pipeline.

### Gitleaks

Scans the repository for accidentally committed secrets.

### pip-audit

Scans Python dependencies for known security vulnerabilities.

Current result:

    No known vulnerabilities found

### Trivy

Scans the Docker image for operating-system vulnerabilities.

The CI pipeline fails when configured HIGH or CRITICAL vulnerabilities are detected.

## Monitoring

The application exposes Prometheus metrics through:

    /metrics

Prometheus scrapes the Kubernetes service:

    production-reliability-api.default.svc.cluster.local:8000

The Prometheus target was verified successfully with:

    up = 1

## Grafana

Grafana is connected to Prometheus and provides application observability.

Dashboard panels include:

1. HTTP Request Rate

2. HTTP Response Status

3. P95 Request Latency

4. Total HTTP Requests

5. Application Instances

6. Application Availability

Grafana data is persisted using a Kubernetes PersistentVolumeClaim.

## Monitoring Architecture

    FastAPI

       |

       | /metrics

       v

    Prometheus

       |

       | PromQL

       v

    Grafana

       |

       v

    Monitoring Dashboard

## Infrastructure Validation

Terraform configuration is validated using:

    terraform fmt -check

    terraform validate

Kubernetes manifests are validated using Kubeconform during CI.

This prevents invalid infrastructure and Kubernetes configuration from progressing through the pipeline.

## Container Registry

Docker images are pushed to GitHub Container Registry.

Images are tagged using the Git commit SHA to provide immutable build references.

Example:

    ghcr.io/thahir2005/devops-production-platform:<commit-sha>

## Verification Results

| Component | Status |

|---|---|

| Python Tests | PASS |

| Docker Build | PASS |

| Terraform Validation | PASS |

| Kubernetes Validation | PASS |

| Monitoring Manifest Validation | PASS |

| Gitleaks | PASS |

| pip-audit | PASS |

| Trivy | PASS |

| GHCR Push | PASS |

| Kubernetes Deployment | PASS |

| 2 Replicas | PASS |

| Readiness Probe | PASS |

| Liveness Probe | PASS |

| Self-Healing | PASS |

| Prometheus Scraping | PASS |

| Grafana Dashboard | PASS |

## Skills Demonstrated

- Linux

- Git

- GitHub

- GitHub Actions

- CI/CD

- Docker

- Kubernetes

- Minikube

- Terraform

- Python

- FastAPI

- GitHub Container Registry

- Prometheus

- Grafana

- Infrastructure Validation

- Container Security

- Dependency Security

- Secret Detection

- DevSecOps

- Application Observability

- Kubernetes Reliability

## Project Goal

The goal of this project is to demonstrate how a production-style application can be built, tested, secured, containerized, deployed, monitored, and automatically recovered using modern DevOps and DevSecOps practices.