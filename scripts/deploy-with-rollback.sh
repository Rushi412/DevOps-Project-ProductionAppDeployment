#!/usr/bin/env bash
set -euo pipefail

IMAGE="${1:?Usage: deploy-with-rollback.sh <repository:immutable-tag>}"
NAMESPACE="${KUBERNETES_NAMESPACE:-social-app}"
DEPLOYMENT="social-platform-app"

kubectl set image "deployment/${DEPLOYMENT}" "${DEPLOYMENT}=${IMAGE}" -n "${NAMESPACE}"

if ! kubectl rollout status "deployment/${DEPLOYMENT}" -n "${NAMESPACE}" --timeout=180s; then
  echo "Rollout failed; restoring the previous ReplicaSet."
  kubectl rollout undo "deployment/${DEPLOYMENT}" -n "${NAMESPACE}"
  kubectl rollout status "deployment/${DEPLOYMENT}" -n "${NAMESPACE}" --timeout=180s
  exit 1
fi

kubectl get deployment "${DEPLOYMENT}" -n "${NAMESPACE}" -o wide
