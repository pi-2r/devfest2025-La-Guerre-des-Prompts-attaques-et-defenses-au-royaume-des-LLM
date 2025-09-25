# Tock GenAI Kubernetes Deployment

This directory contains Kubernetes manifests and deployment scripts for running the Tock GenAI stack on Kubernetes. The deployment includes all components from the original Docker Compose setup, enhanced with Kubernetes-native features for production use.

## 📋 Prerequisites

- Kubernetes cluster (v1.25+)
- kubectl configured to access your cluster
- At least 8 CPU cores and 16GB RAM available
- 100GB of storage for persistent volumes
- Ingress controller (nginx, traefik, etc.) for external access

## 🏗️ Architecture Overview

The deployment consists of:

### Core Services
- **MongoDB Replica Set**: 3-node MongoDB cluster for data persistence
- **PostgreSQL**: Database with pgvector extension for vector operations
- **Tock NLP API**: Natural language processing service
- **Tock Bot API**: Bot conversation management
- **Admin Web**: Web administration interface
- **Build Worker**: Background processing service

### AI/ML Services
- **NeMo Guardrails**: NVIDIA's AI safety framework
- **NeMo Proxy**: Security-enhanced proxy with LLM protections
- **GenAI Orchestrator**: Vector store and AI orchestration
- **Langfuse**: LLM observability and analytics

### Infrastructure
- **Monitoring**: Prometheus and Grafana for observability
- **Auto-scaling**: Horizontal Pod Autoscalers
- **Network Security**: Network policies for service isolation
- **Resource Management**: Resource quotas and limits

## 📁 File Structure

```
kubernetes/
├── 00-namespace.yaml          # Kubernetes namespace
├── 01-configmap.yaml          # Configuration (non-sensitive)
├── 02-secrets.yaml            # Sensitive configuration
├── 03-persistent-volumes.yaml # Storage definitions
├── 04-mongodb.yaml            # MongoDB replica set
├── 05-mongo-setup.yaml        # MongoDB initialization
├── 06-postgresql.yaml         # PostgreSQL database
├── 07-nemo-guardrails.yaml    # AI safety service
├── 08-nemo-proxy.yaml          # Security proxy
├── 09-tock-apis.yaml           # Tock NLP and Bot APIs
├── 10-gen-ai-orchestrator.yaml # AI orchestration
├── 11-tock-services.yaml       # Admin web and build worker
├── 12-langfuse.yaml            # LLM observability
├── 13-ingress.yaml             # External access configuration
├── 14-hpa.yaml                 # Auto-scaling rules
├── 15-network-policies.yaml    # Network security
├── 16-resource-quotas.yaml     # Resource limits
├── 17-monitoring.yaml          # Prometheus and Grafana
├── deploy.sh                   # Deployment script
├── undeploy.sh                 # Cleanup script
├── backup.sh                   # Database backup script
├── restore.sh                  # Database restore script
└── README.md                   # This file
```

## 🚀 Quick Start

### 1. Deploy the Stack

```bash
# Make scripts executable
chmod +x deploy.sh undeploy.sh backup.sh restore.sh

# Deploy everything
./deploy.sh
```

### 2. Access the Services

After deployment, you can access:

```bash
# Admin Web Interface (port-forward)
kubectl port-forward service/admin-web 8080:8080 -n tock-genai

# Or via Ingress (configure DNS first)
# Add to /etc/hosts: <ingress-ip> tock-genai.local
# Access: http://tock-genai.local/
```

### 3. Monitor the Deployment

```bash
# Check pod status
kubectl get pods -n tock-genai

# Check services
kubectl get services -n tock-genai

# View logs
kubectl logs -f deployment/admin-web -n tock-genai

# Access monitoring
kubectl port-forward service/grafana 3000:3000 -n tock-genai
# Grafana: http://localhost:3000 (admin/admin)
```

## ⚙️ Configuration

### Environment Variables

Key configuration is managed through ConfigMaps and Secrets:

- **ConfigMap**: Non-sensitive settings (database URLs, service URLs)
- **Secrets**: Sensitive data (passwords, API keys)

### Important Settings

Update these in `02-secrets.yaml` before deployment:

```yaml
# Base64 encoded values
OPENAI_API_KEY: <your-openai-api-key-base64>
POSTGRES_PASSWORD: <postgres-password-base64>
LANGFUSE_DB_PASSWORD: <langfuse-password-base64>
```

Encode values using: `echo -n "your-value" | base64`

### Resource Limits

Default resource allocations per service:

| Service | CPU Request | Memory Request | CPU Limit | Memory Limit |
|---------|-------------|----------------|-----------|--------------|
| MongoDB | 500m | 1Gi | 1 | 2Gi |
| PostgreSQL | 300m | 512Mi | 1 | 2Gi |
| NeMo Proxy | 200m | 512Mi | 500m | 1Gi |
| Admin Web | 200m | 256Mi | 500m | 1Gi |
| Others | 100m | 128Mi | 500m | 512Mi |

## 🔒 Security Features

### Network Policies
- Services can only communicate with authorized dependencies
- External access is restricted to ingress-enabled services
- Database access is limited to application services

### Resource Quotas
- Namespace-level limits prevent resource exhaustion
- Pod-level limits ensure fair resource sharing
- Storage quotas prevent unlimited disk usage

### Secrets Management
- Sensitive data is stored in Kubernetes Secrets
- Base64 encoding for secure transmission
- Environment variable injection for applications

## 📊 Monitoring and Observability

### Prometheus Metrics
- Application performance metrics
- Resource utilization monitoring
- Custom alerts for critical conditions

### Grafana Dashboards
- Real-time performance visualization
- Historical trend analysis
- Alert visualization

### Access Monitoring
```bash
# Prometheus
kubectl port-forward service/prometheus 9090:9090 -n tock-genai

# Grafana (admin/admin)
kubectl port-forward service/grafana 3000:3000 -n tock-genai
```

## 🔄 Scaling

### Horizontal Pod Autoscaler
Auto-scaling is configured for critical services:

```bash
# Check HPA status
kubectl get hpa -n tock-genai

# Services with auto-scaling:
# - nemo-proxy: 2-5 replicas (CPU 70%)
# - admin-web: 1-3 replicas (CPU 80%)
# - gen-ai-orchestrator: 1-3 replicas (CPU 70%)
```

### Manual Scaling
```bash
# Scale specific deployments
kubectl scale deployment admin-web --replicas=3 -n tock-genai
kubectl scale deployment nemo-proxy --replicas=4 -n tock-genai
```

## 💾 Backup and Restore

### Create Backup
```bash
# Create backup of databases and configurations
./backup.sh

# Backup file will be created in ./backups/
```

### Restore from Backup
```bash
# Restore from backup file
./restore.sh ./backups/20231201-120000.tar.gz
```

### What's Backed Up
- MongoDB databases (all collections)
- PostgreSQL databases (all databases)
- Kubernetes configurations (manifests)
- Backup metadata and restore instructions

## 🐛 Troubleshooting

### Common Issues

#### Pods Stuck in Pending
```bash
# Check resource availability
kubectl describe nodes
kubectl get events -n tock-genai --sort-by='.lastTimestamp'

# Check PVC status
kubectl get pvc -n tock-genai
```

#### Database Connection Issues
```bash
# Check database pod logs
kubectl logs -f deployment/postgresql -n tock-genai
kubectl logs -f statefulset/mongo -n tock-genai

# Test database connectivity
kubectl exec -it deployment/postgresql -n tock-genai -- psql -U postgres -l
```

#### Service Discovery Issues
```bash
# Check service endpoints
kubectl get endpoints -n tock-genai

# Test internal connectivity
kubectl exec -it deployment/admin-web -n tock-genai -- nslookup postgresql
```

### Debugging Commands

```bash
# Get comprehensive status
kubectl get all -n tock-genai

# Check resource usage
kubectl top pods -n tock-genai
kubectl top nodes

# View detailed pod information
kubectl describe pod <pod-name> -n tock-genai

# Check network policies
kubectl get networkpolicy -n tock-genai
```

## 🔧 Customization

### Adding New Services
1. Create deployment manifest following existing patterns
2. Add service discovery configuration
3. Update network policies if needed
4. Add monitoring configuration
5. Update deployment scripts

### Modifying Resource Limits
Edit the respective YAML files and update:
- `resources.requests` and `resources.limits` in deployments
- Resource quotas in `16-resource-quotas.yaml`
- HPA targets in `14-hpa.yaml`

### Custom Ingress Configuration
Modify `13-ingress.yaml` to:
- Change hostname
- Add TLS certificates
- Configure additional paths
- Set up authentication

## 📚 Additional Resources

- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Tock Framework](https://doc.tock.ai/)
- [NVIDIA NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails)
- [Langfuse Documentation](https://langfuse.com/docs)

## 🤝 Contributing

1. Test changes in a development cluster
2. Update documentation for any configuration changes
3. Ensure all services remain functional after modifications
4. Update resource requirements if needed

## 📄 License

This deployment configuration follows the same license as the Tock framework and related components.
