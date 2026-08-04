# GitOps deployment

`application.yaml` is an Argo CD application definition for the EKS overlay. Applying it requires an existing Kubernetes cluster with Argo CD installed. This repository does not install or provision a paid cluster automatically.

Before an approved deployment:

1. Replace `replace-with-immutable-tag` in the EKS kustomization with a built image tag.
2. Render the overlay with `kubectl kustomize deploy/kubernetes/overlays/eks`.
3. Review the diff and confirm that no secrets are stored in Git.
4. Apply the Argo CD application and monitor health and synchronization.

Argo CD continuously reconciles the declared manifests. The deployment strategy, readiness probes, and disruption budget protect rolling releases.
