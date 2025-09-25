#!/bin/bash

# Tock GenAI Kubernetes Cleanup Script
# This script removes the entire Tock GenAI stack from Kubernetes

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

# Confirmation prompt
read -p "Are you sure you want to delete the entire Tock GenAI deployment? This will remove all data! (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    print_status "Deployment cleanup cancelled"
    exit 0
fi

print_status "Starting Tock GenAI cleanup from Kubernetes..."

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Array of manifest files in reverse deployment order
MANIFESTS=(
    "17-monitoring.yaml"
    "16-resource-quotas.yaml"
    "15-network-policies.yaml"
    "14-hpa.yaml"
    "13-ingress.yaml"
    "12-langfuse.yaml"
    "11-tock-services.yaml"
    "10-gen-ai-orchestrator.yaml"
    "09-tock-apis.yaml"
    "08-nemo-proxy.yaml"
    "07-nemo-guardrails.yaml"
    "06-postgresql.yaml"
    "05-mongo-setup.yaml"
    "04-mongodb.yaml"
    "03-persistent-volumes.yaml"
    "02-secrets.yaml"
    "01-configmap.yaml"
    "00-namespace.yaml"
)

# Delete each manifest
for manifest in "${MANIFESTS[@]}"; do
    manifest_path="$SCRIPT_DIR/$manifest"
    
    if [[ -f "$manifest_path" ]]; then
        print_status "Deleting resources from $manifest..."
        if kubectl delete -f "$manifest_path" --ignore-not-found=true; then
            print_success "Deleted resources from $manifest"
        else
            print_warning "Some resources from $manifest may not have been deleted"
        fi
    else
        print_warning "Manifest $manifest not found, skipping..."
    fi
done

# Force delete namespace if it still exists
print_status "Ensuring namespace is completely removed..."
kubectl delete namespace tock-genai --ignore-not-found=true --timeout=60s

print_success "Tock GenAI cleanup completed!"

# Check for any remaining resources
REMAINING_PODS=$(kubectl get pods -n tock-genai 2>/dev/null | wc -l || echo "0")
if [[ $REMAINING_PODS -gt 0 ]]; then
    print_warning "Some pods may still be terminating. Check with: kubectl get pods -n tock-genai"
fi

print_status "Cleanup summary completed. All Tock GenAI resources have been removed."
