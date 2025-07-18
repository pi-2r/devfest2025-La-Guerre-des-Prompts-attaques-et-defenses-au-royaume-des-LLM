#!/bin/bash

# Tock GenAI Pre-deployment Validation Script
# This script checks if the environment is ready for deployment

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[✓]${NC} $1"
}

print_error() {
    echo -e "${RED}[✗]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[!]${NC} $1"
}

# Track validation status
VALIDATION_PASSED=true

print_status "Tock GenAI Kubernetes Deployment Validation"
echo "=============================================="

# Check kubectl
print_status "Checking kubectl availability..."
if command -v kubectl &> /dev/null; then
    KUBECTL_VERSION=$(kubectl version --client --short 2>/dev/null | cut -d' ' -f3)
    print_success "kubectl is available (version: $KUBECTL_VERSION)"
else
    print_error "kubectl is not installed or not in PATH"
    VALIDATION_PASSED=false
fi

# Check cluster connectivity
print_status "Checking Kubernetes cluster connectivity..."
if kubectl cluster-info &> /dev/null; then
    CLUSTER_VERSION=$(kubectl version --short 2>/dev/null | grep "Server Version" | cut -d' ' -f3)
    print_success "Connected to Kubernetes cluster (version: $CLUSTER_VERSION)"
else
    print_error "Cannot connect to Kubernetes cluster"
    VALIDATION_PASSED=false
fi

# Check cluster resources
print_status "Checking cluster resources..."
if kubectl get nodes &> /dev/null; then
    NODE_COUNT=$(kubectl get nodes --no-headers | wc -l)
    print_success "Cluster has $NODE_COUNT nodes"
    
    # Check CPU and memory
    TOTAL_CPU=$(kubectl describe nodes | grep -A 5 "Allocatable:" | grep "cpu:" | awk '{sum += $2} END {print sum}')
    TOTAL_MEMORY=$(kubectl describe nodes | grep -A 5 "Allocatable:" | grep "memory:" | awk '{sum += $2} END {print sum}')
    
    if [[ $TOTAL_CPU -ge 8 ]]; then
        print_success "Sufficient CPU resources available ($TOTAL_CPU cores)"
    else
        print_warning "Limited CPU resources ($TOTAL_CPU cores). Recommended: 8+ cores"
    fi
    
    print_success "Memory resources: $TOTAL_MEMORY"
else
    print_error "Cannot access cluster nodes"
    VALIDATION_PASSED=false
fi

# Check for required storage class
print_status "Checking storage classes..."
if kubectl get storageclass &> /dev/null; then
    STORAGE_CLASSES=$(kubectl get storageclass --no-headers | wc -l)
    DEFAULT_SC=$(kubectl get storageclass | grep "(default)" | awk '{print $1}')
    
    if [[ $STORAGE_CLASSES -gt 0 ]]; then
        print_success "Storage classes available: $STORAGE_CLASSES"
        if [[ -n "$DEFAULT_SC" ]]; then
            print_success "Default storage class: $DEFAULT_SC"
        else
            print_warning "No default storage class found. You may need to specify storageClassName in PVCs"
        fi
    else
        print_error "No storage classes found"
        VALIDATION_PASSED=false
    fi
else
    print_error "Cannot access storage classes"
    VALIDATION_PASSED=false
fi

# Check for ingress controller
print_status "Checking ingress controller..."
INGRESS_CONTROLLERS=$(kubectl get pods --all-namespaces | grep -E "(ingress|nginx|traefik)" | wc -l)
if [[ $INGRESS_CONTROLLERS -gt 0 ]]; then
    print_success "Ingress controller detected"
else
    print_warning "No ingress controller detected. External access may not work"
fi

# Check if namespace already exists
print_status "Checking if tock-genai namespace exists..."
if kubectl get namespace tock-genai &> /dev/null; then
    print_warning "Namespace 'tock-genai' already exists. Deployment will update existing resources"
else
    print_success "Namespace 'tock-genai' does not exist (will be created)"
fi

# Check manifest files
print_status "Checking Kubernetes manifest files..."
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

REQUIRED_FILES=(
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

MISSING_FILES=0
for file in "${REQUIRED_FILES[@]}"; do
    if [[ -f "$SCRIPT_DIR/$file" ]]; then
        print_success "Found: $file"
    else
        print_error "Missing: $file"
        MISSING_FILES=$((MISSING_FILES + 1))
        VALIDATION_PASSED=false
    fi
done

if [[ $MISSING_FILES -eq 0 ]]; then
    print_success "All required manifest files are present"
fi

# Check secrets configuration
print_status "Checking secrets configuration..."
if grep -q "changeme" "$SCRIPT_DIR/02-secrets.yaml" 2>/dev/null; then
    print_warning "Default passwords detected in secrets.yaml. Please update before production deployment"
else
    print_success "Secrets appear to be configured"
fi

# Summary
echo ""
echo "=============================================="
if [[ $VALIDATION_PASSED == true ]]; then
    print_success "Validation PASSED - Ready for deployment!"
    echo ""
    print_status "To deploy: ./deploy.sh"
    print_status "To monitor: kubectl get pods -n tock-genai"
    print_status "To access: kubectl port-forward service/admin-web 8080:8080 -n tock-genai"
else
    print_error "Validation FAILED - Please fix the issues above before deployment"
    exit 1
fi
