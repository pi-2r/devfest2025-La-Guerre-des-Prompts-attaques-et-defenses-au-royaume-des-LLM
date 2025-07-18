#!/bin/bash

# Tock GenAI Restore Script
# This script restores MongoDB and PostgreSQL databases from backup

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
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

# Check arguments
if [[ $# -ne 1 ]]; then
    print_error "Usage: $0 <backup-file.tar.gz>"
    print_error "Example: $0 ./backups/20231201-120000.tar.gz"
    exit 1
fi

BACKUP_FILE="$1"
NAMESPACE="tock-genai"
RESTORE_DIR="./restore-$(date +%Y%m%d-%H%M%S)"

# Check if backup file exists
if [[ ! -f "$BACKUP_FILE" ]]; then
    print_error "Backup file not found: $BACKUP_FILE"
    exit 1
fi

print_warning "This will restore data and may overwrite existing data!"
read -p "Are you sure you want to continue? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    print_status "Restore cancelled"
    exit 0
fi

print_status "Starting restore process..."
print_status "Backup file: $BACKUP_FILE"

# Extract backup
print_status "Extracting backup..."
mkdir -p "$RESTORE_DIR"
tar -xzf "$BACKUP_FILE" -C "$RESTORE_DIR" --strip-components=1

# Check if required files exist
if [[ ! -d "$RESTORE_DIR/mongodb-backup" ]] || [[ ! -f "$RESTORE_DIR/postgres-backup.sql" ]]; then
    print_error "Invalid backup file structure"
    exit 1
fi

# Ensure namespace exists
print_status "Checking namespace..."
if ! kubectl get namespace $NAMESPACE &> /dev/null; then
    print_error "Namespace $NAMESPACE does not exist. Please deploy the application first."
    exit 1
fi

# Wait for pods to be ready
print_status "Waiting for database pods to be ready..."
kubectl wait --for=condition=ready pod -l app=mongo -n $NAMESPACE --timeout=300s
kubectl wait --for=condition=ready pod -l app=postgresql -n $NAMESPACE --timeout=300s

# Restore MongoDB
print_status "Restoring MongoDB..."

MONGO_POD=$(kubectl get pods -n $NAMESPACE -l app=mongo -o jsonpath='{.items[0].metadata.name}')

if [[ -z "$MONGO_POD" ]]; then
    print_error "MongoDB pod not found"
    exit 1
fi

# Copy backup to MongoDB pod
kubectl cp "$RESTORE_DIR/mongodb-backup" $NAMESPACE/$MONGO_POD:/tmp/

# Drop existing databases and restore
kubectl exec -n $NAMESPACE $MONGO_POD -- mongorestore --host localhost:27017 --drop /tmp/mongodb-backup

print_success "MongoDB restore completed"

# Restore PostgreSQL
print_status "Restoring PostgreSQL..."

POSTGRES_POD=$(kubectl get pods -n $NAMESPACE -l app=postgresql -o jsonpath='{.items[0].metadata.name}')

if [[ -z "$POSTGRES_POD" ]]; then
    print_error "PostgreSQL pod not found"
    exit 1
fi

# Copy backup to PostgreSQL pod and restore
kubectl cp "$RESTORE_DIR/postgres-backup.sql" $NAMESPACE/$POSTGRES_POD:/tmp/
kubectl exec -n $NAMESPACE $POSTGRES_POD -- psql -U postgres -f /tmp/postgres-backup.sql

print_success "PostgreSQL restore completed"

# Restart services to ensure they pick up restored data
print_status "Restarting services..."
kubectl rollout restart deployment -n $NAMESPACE
kubectl rollout status deployment --all -n $NAMESPACE --timeout=300s

print_success "Services restarted successfully"

# Cleanup
rm -rf "$RESTORE_DIR"

print_success "Restore completed successfully!"
print_status "All services have been restarted and should be using the restored data"

# Show current status
print_status "Current pod status:"
kubectl get pods -n $NAMESPACE
