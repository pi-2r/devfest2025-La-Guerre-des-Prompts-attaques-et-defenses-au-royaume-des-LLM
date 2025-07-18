#!/bin/bash

# Tock GenAI Kubernetes Deployment Script
# This script deploys the entire Tock GenAI stack to Kubernetes

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if kubectl is available
if ! command -v kubectl &> /dev/null; then
    print_error "kubectl is not installed or not in PATH"
    exit 1
fi

# Check if we can connect to Kubernetes cluster
if ! kubectl cluster-info &> /dev/null; then
    print_error "Cannot connect to Kubernetes cluster. Please check your kubeconfig"
    exit 1
fi

print_status "Starting Tock GenAI deployment to Kubernetes..."

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Array of manifest files in deployment order
MANIFESTS=(
    "00-namespace.yaml"
    "01-configmap.yaml"
    "02-secrets.yaml"
    "03-persistent-volumes.yaml"
    "04-mongodb.yaml"
    "05-mongo-setup.yaml"
    "06-postgresql.yaml"
    "07-nemo-guardrails.yaml"
    "08-nemo-proxy.yaml"
    "09-tock-apis.yaml"
    "10-gen-ai-orchestrator.yaml"
    "11-tock-services.yaml"
    "12-langfuse.yaml"
    "13-ingress.yaml"
    "14-hpa.yaml"
    "15-network-policies.yaml"
    "16-resource-quotas.yaml"
    "17-monitoring.yaml"
)

# Deploy each manifest
for manifest in "${MANIFESTS[@]}"; do
    manifest_path="$SCRIPT_DIR/$manifest"
    
    if [[ -f "$manifest_path" ]]; then
        print_status "Applying $manifest..."
        if kubectl apply -f "$manifest_path"; then
            print_success "Applied $manifest"
        else
            print_error "Failed to apply $manifest"
            exit 1
        fi
    else
        print_warning "Manifest $manifest not found, skipping..."
    fi
done

print_status "Waiting for MongoDB replica set initialization..."
kubectl wait --for=condition=complete job/mongo-setup -n tock-genai --timeout=300s

print_status "Waiting for PostgreSQL to be ready..."
kubectl wait --for=condition=ready pod -l app=postgresql -n tock-genai --timeout=300s

print_status "Waiting for all deployments to be ready..."
kubectl wait --for=condition=available deployment --all -n tock-genai --timeout=600s

print_success "Tock GenAI deployment completed successfully!"

print_status "Getting service information..."
kubectl get services -n tock-genai

print_status "Getting pod status..."
kubectl get pods -n tock-genai

print_status "Getting ingress information..."
kubectl get ingress -n tock-genai

echo ""
print_success "Deployment Summary:"
echo "- Namespace: tock-genai"
echo "- Services: $(kubectl get services -n tock-genai --no-headers | wc -l) services deployed"
echo "- Pods: $(kubectl get pods -n tock-genai --no-headers | wc -l) pods running"
echo "- Access the admin interface via the ingress or port-forward:"
echo "  kubectl port-forward service/admin-web 8080:8080 -n tock-genai"

print_warning "Note: Make sure to update your /etc/hosts file or DNS to point tock-genai.local to your ingress IP"
