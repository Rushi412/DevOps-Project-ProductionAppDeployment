# Runbook

## Local development

```powershell
.\mvnw.cmd clean test
.\mvnw.cmd spring-boot:run
```

Open `http://localhost:8080` after startup. The H2 console is only enabled in the default `local` profile.

## Docker

```powershell
docker build -t social-platform-app:local -f deploy/docker/Dockerfile .
docker run --rm -p 8080:8080 social-platform-app:local
```

## kind local Kubernetes

Start Docker Desktop, then follow [the local deployment guide](../deploy/kubernetes/local/README.md) to create and use the standalone kind cluster.

## Kubernetes validation

```powershell
kubectl apply --dry-run=client -f deploy/kubernetes/base
```

## Terraform study reference

```powershell
Set-Location infrastructure/terraform
terraform fmt -recursive
terraform init
terraform validate
terraform plan
```

EKS is not the recommended learning path and is not free. If you intentionally provision it, remove billable resources deliberately:

```powershell
terraform destroy
```
