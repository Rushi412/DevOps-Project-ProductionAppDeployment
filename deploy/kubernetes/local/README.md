# kind local Kubernetes

This project uses a standalone [kind](https://kind.sigs.k8s.io/) cluster for no-cost local learning. It uses the Docker Desktop engine but does not depend on Docker Desktop's managed Kubernetes feature. No AWS account or EKS cluster is required.

## One-time setup

1. Start Docker Desktop and wait until its engine is running.
2. Create the dedicated local cluster:

```powershell
kind create cluster --name social-platform --wait 2m
kubectl config use-context kind-social-platform
kubectl get nodes
```

## Deploy locally

Build the application image and load it directly into kind:

```powershell
docker build -t rushi412/social-platform-app:local -f deploy/docker/Dockerfile .
kind load docker-image rushi412/social-platform-app:local --name social-platform
```

The local manifests use the in-memory H2 `local` profile, so no database installation or secret is required. Apply the manifests:

```powershell
kubectl apply -f deploy/kubernetes/base/namespace.yaml
kubectl apply -f deploy/kubernetes/base/configmap.yaml
kubectl apply -f deploy/kubernetes/base/service.yaml
kubectl apply -f deploy/kubernetes/base/deployment.yaml
kubectl rollout status deployment/social-platform-app -n social-app
```

For a quick local test, port-forward the service:

```powershell
kubectl port-forward service/social-platform-app 8080:80 -n social-app
```

Open `http://localhost:8080` and stop port forwarding with `Ctrl+C`.

## Clean up

```powershell
kind delete cluster --name social-platform
```
