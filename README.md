# platform-infra

Platform infrastructure repository containing Kubernetes manifests, Helm charts, Docker configuration, and Argo CD GitOps deployments.

## Overview

This repository manages the infrastructure, deployment configurations, and operational resources required to run the platform in Kubernetes environments.

The project follows GitOps principles using Argo CD to automate application deployment and infrastructure synchronization.

## Technology Stack

* Kubernetes
* Helm
* Argo CD
* Docker
* Python
* GitHub

## Repository Structure

```text
platform-infra/
├── charts/             # Helm charts
├── k8s/                # Kubernetes manifests
├── src/                # Application source code
├── Dockerfile          # Container image definition
├── requirements.txt    # Python dependencies
├── .gitignore
└── README.md
```

## Prerequisites

Before getting started, ensure the following tools are installed:

* Docker
* Kubernetes Cluster
* kubectl
* Helm
* Argo CD CLI (optional)
* Python 3.12+

## Local Development

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Build Docker Image

```bash
docker build -t platform-infra:latest .
```

## Kubernetes Deployment

Apply Kubernetes manifests:

```bash
kubectl apply -f k8s/
```

Verify deployment:

```bash
kubectl get pods
kubectl get services
```

## Helm Deployment

Install the Helm chart:

```bash
helm install platform ./charts
```

Upgrade deployment:

```bash
helm upgrade platform ./charts
```

## Argo CD Deployment

Create or update the Argo CD application to continuously synchronize infrastructure and application resources from this repository.

Example:

```bash
argocd app create platform \
  --repo <repository-url> \
  --path charts \
  --dest-server https://kubernetes.default.svc \
  --dest-namespace default
```

Synchronize:

```bash
argocd app sync platform
```

## GitOps Workflow

1. Make infrastructure or application changes.
2. Commit and push changes to the repository.
3. Argo CD detects updates.
4. Changes are automatically synchronized to the cluster.
5. Deployment status can be monitored through the Argo CD UI.

## Security

* Do not commit secrets or credentials.
* Use Kubernetes Secrets or an external secret management solution.
* Keep dependencies updated.
* Follow least-privilege access principles.

## Contributing

1. Create a feature branch.
2. Implement changes.
3. Submit a pull request.
4. Ensure all deployments and validations pass before merging.

## License

Internal use only unless otherwise specified.

