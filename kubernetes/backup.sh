#!/bin/bash

# Tock GenAI Backup Script
# This script creates backups of MongoDB and PostgreSQL databases

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

# Configuration
NAMESPACE="tock-genai"
BACKUP_DIR="./backups/$(date +%Y%m%d-%H%M%S)"
MONGODB_BACKUP_NAME="mongodb-backup"
POSTGRES_BACKUP_NAME="postgres-backup"

# Create backup directory
mkdir -p "$BACKUP_DIR"

print_status "Starting backup process..."
print_status "Backup directory: $BACKUP_DIR"

# Backup MongoDB
print_status "Backing up MongoDB..."

# Get MongoDB pod
MONGO_POD=$(kubectl get pods -n $NAMESPACE -l app=mongo -o jsonpath='{.items[0].metadata.name}')

if [[ -z "$MONGO_POD" ]]; then
    print_error "MongoDB pod not found"
    exit 1
fi

# Create MongoDB backup
kubectl exec -n $NAMESPACE $MONGO_POD -- mongodump --host localhost:27017 --out /tmp/mongodb-backup
kubectl cp $NAMESPACE/$MONGO_POD:/tmp/mongodb-backup "$BACKUP_DIR/$MONGODB_BACKUP_NAME"

print_success "MongoDB backup completed"

# Backup PostgreSQL
print_status "Backing up PostgreSQL..."

# Get PostgreSQL pod
POSTGRES_POD=$(kubectl get pods -n $NAMESPACE -l app=postgresql -o jsonpath='{.items[0].metadata.name}')

if [[ -z "$POSTGRES_POD" ]]; then
    print_error "PostgreSQL pod not found"
    exit 1
fi

# Create PostgreSQL backup
kubectl exec -n $NAMESPACE $POSTGRES_POD -- pg_dumpall -U postgres > "$BACKUP_DIR/$POSTGRES_BACKUP_NAME.sql"

print_success "PostgreSQL backup completed"

# Backup Kubernetes manifests
print_status "Backing up Kubernetes configurations..."
kubectl get all,configmaps,secrets,pvc,ingress,networkpolicy -n $NAMESPACE -o yaml > "$BACKUP_DIR/kubernetes-manifests.yaml"

print_success "Kubernetes configurations backed up"

# Create backup metadata
cat > "$BACKUP_DIR/backup-metadata.txt" << EOF
Tock GenAI Backup Metadata
==========================
Backup Date: $(date)
Kubernetes Namespace: $NAMESPACE
MongoDB Pod: $MONGO_POD
PostgreSQL Pod: $POSTGRES_POD

Files:
- $MONGODB_BACKUP_NAME/: MongoDB database dump
- $POSTGRES_BACKUP_NAME.sql: PostgreSQL database dump
- kubernetes-manifests.yaml: Kubernetes resource definitions
- backup-metadata.txt: This metadata file

Restore Instructions:
1. Use restore.sh script in the same directory
2. Or manually restore using kubectl and database tools
EOF

print_success "Backup completed successfully!"
print_status "Backup location: $BACKUP_DIR"
print_status "Total backup size: $(du -sh $BACKUP_DIR | cut -f1)"

# Compress backup
print_status "Compressing backup..."
tar -czf "$BACKUP_DIR.tar.gz" -C "$(dirname $BACKUP_DIR)" "$(basename $BACKUP_DIR)"
rm -rf "$BACKUP_DIR"

print_success "Backup compressed: $BACKUP_DIR.tar.gz"
