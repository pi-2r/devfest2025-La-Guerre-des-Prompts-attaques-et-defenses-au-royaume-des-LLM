#!/bin/bash

# Tock GenAI Status Monitoring Script
# This script provides a quick overview of the deployment status

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_header() {
    echo -e "${BLUE}$1${NC}"
    echo "$(printf '=%.0s' {1..50})"
}

print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[✓]${NC} $1"
}

print_error() {
    echo -e "${RED}[✗]${NC} $1"
}

NAMESPACE="tock-genai"

# Check if namespace exists
if ! kubectl get namespace $NAMESPACE &> /dev/null; then
    print_error "Namespace '$NAMESPACE' not found. Please deploy first using ./deploy.sh"
    exit 1
fi

clear
echo -e "${GREEN}Tock GenAI Kubernetes Status Dashboard${NC}"
echo "======================================"
echo "Namespace: $NAMESPACE"
echo "Timestamp: $(date)"
echo ""

# Pod Status
print_header "Pod Status"
kubectl get pods -n $NAMESPACE -o custom-columns="NAME:.metadata.name,STATUS:.status.phase,READY:.status.containerStatuses[0].ready,RESTARTS:.status.containerStatuses[0].restartCount,AGE:.metadata.creationTimestamp" --sort-by='.metadata.name'
echo ""

# Service Status
print_header "Service Status"
kubectl get services -n $NAMESPACE -o custom-columns="NAME:.metadata.name,TYPE:.spec.type,CLUSTER-IP:.spec.clusterIP,EXTERNAL-IP:.status.loadBalancer.ingress[0].ip,PORT:.spec.ports[0].port"
echo ""

# Storage Status
print_header "Storage Status"
kubectl get pvc -n $NAMESPACE -o custom-columns="NAME:.metadata.name,STATUS:.status.phase,VOLUME:.spec.volumeName,CAPACITY:.status.capacity.storage,ACCESS:.spec.accessModes[0]"
echo ""

# HPA Status
print_header "Auto-scaling Status"
if kubectl get hpa -n $NAMESPACE &> /dev/null; then
    kubectl get hpa -n $NAMESPACE
else
    echo "No HPAs found"
fi
echo ""

# Resource Usage (if metrics-server is available)
print_header "Resource Usage"
if kubectl top pods -n $NAMESPACE &> /dev/null; then
    kubectl top pods -n $NAMESPACE
else
    echo "Metrics not available (metrics-server may not be installed)"
fi
echo ""

# Recent Events
print_header "Recent Events (Last 10)"
kubectl get events -n $NAMESPACE --sort-by='.lastTimestamp' --no-headers | tail -10 | while read line; do
    if [[ $line == *"Warning"* ]]; then
        echo -e "${YELLOW}$line${NC}"
    elif [[ $line == *"Error"* ]] || [[ $line == *"Failed"* ]]; then
        echo -e "${RED}$line${NC}"
    else
        echo -e "${GREEN}$line${NC}"
    fi
done
echo ""

# Quick Health Check
print_header "Quick Health Check"

# Check critical pods
CRITICAL_PODS=("mongo" "postgresql" "admin-web" "nemo-proxy")
for pod in "${CRITICAL_PODS[@]}"; do
    if kubectl get pods -n $NAMESPACE -l "app=$pod" -o jsonpath='{.items[0].status.phase}' 2>/dev/null | grep -q "Running"; then
        print_success "$pod is running"
    else
        print_error "$pod is not running properly"
    fi
done

echo ""

# Access Information
print_header "Access Information"
echo "Local Access (port-forward):"
echo "  Admin Web:    kubectl port-forward service/admin-web 8080:8080 -n $NAMESPACE"
echo "  Grafana:      kubectl port-forward service/grafana 3000:3000 -n $NAMESPACE"
echo "  Prometheus:   kubectl port-forward service/prometheus 9090:9090 -n $NAMESPACE"
echo ""

INGRESS_IP=$(kubectl get ingress -n $NAMESPACE -o jsonpath='{.items[0].status.loadBalancer.ingress[0].ip}' 2>/dev/null)
if [[ -n "$INGRESS_IP" ]]; then
    echo "Ingress Access:"
    echo "  Add to /etc/hosts: $INGRESS_IP tock-genai.local"
    echo "  Access: http://tock-genai.local/"
else
    echo "Ingress: External IP not yet assigned"
fi

echo ""
print_status "Status check completed. Use 'kubectl logs -f <pod-name> -n $NAMESPACE' for detailed logs"
