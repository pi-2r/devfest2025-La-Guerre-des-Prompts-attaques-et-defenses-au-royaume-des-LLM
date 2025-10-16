# TOCK GenAI Stack with NeMo Guardrails

This Docker Compose setup provides a complete chatbot platform with AI safety features using TOCK framework and NeMo Guardrails.

## 🏗️ Architecture Overview

The stack includes:
- **TOCK Framework**: Conversational AI platform (MongoDB cluster, NLP API, Bot API, Admin Web)
- **NeMo Guardrails**: AI safety layer for prompt injection protection
- **NeMo Proxy**: Custom proxy service with security features
- **PostgreSQL with pgvector**: Vector database for RAG capabilities
- **Langfuse**: LLM observability and analytics
- **Gen AI Orchestrator**: AI orchestration service

## 📋 Prerequisites

### System Requirements
- Docker and Docker Compose installed
- At least **40GB** free disk space
- **8GB RAM** minimum (16GB recommended)
- Configure `vm.max_map_count` for OpenSearch compatibility:
  ```bash
  # On Linux/macOS
  sudo sysctl -w vm.max_map_count=262144
  
  # To make it permanent
  echo 'vm.max_map_count=262144' | sudo tee -a /etc/sysctl.conf
  ```

### Environment Configuration
1. Copy the appropriate environment template:
   ```bash
   # For ARM64 (Apple M1/M2/M3)
   cp template-arm64.env .env
   
   # For AMD64/x86_64
   cp template.env .env
   
   # For internet deployment
   cp template-internet.env .env
   ```

2. Configure your OpenAI API key (required for NeMo Guardrails):
   ```bash
   export OPENAI_API_KEY="your-openai-api-key-here"
   ```

## 🚀 Quick Start

### 1. Launch the Full Stack
```bash
# Load environment variables
source .env

# Start all services
docker-compose -f docker-compose-genai.yml up -d
```

### 2. Check Services Status
```bash
# View all running containers
docker-compose -f docker-compose-genai.yml ps

# Check logs for specific service
docker-compose -f docker-compose-genai.yml logs -f nemo-proxy
```

### 3. Access Web Interfaces
Once all services are running:
- **TOCK Admin**: http://localhost (port 80)
- **Langfuse**: http://localhost:3000
- **NeMo Guardrails**: http://localhost:8001
- **NeMo Proxy**: http://localhost:8002
- **Bot API**: http://localhost:8080
- **NLP API**: http://localhost:8888
- **Gen AI Orchestrator**: http://localhost:8000

## 🔐 Default Credentials

### TOCK Admin Interface
- **Users**: `admin@app.com`, `user@app.com`, `techadmin@app.com`
- **Password**: `password`
- **Roles**: Various roles available (admin, user, technical admin)

### Database Access
- **PostgreSQL**:
    - Host: `localhost:5433`
    - User: `postgres`
    - Password: `ChangeMe`
    - Database: `postgres`

## 🛠️ Development with NeMo Proxy

### Local Development Setup

1. **Navigate to nemo-proxy directory**:
   ```bash
   cd nemo-proxy
   ```

2. **Create Python virtual environment**:
   ```bash
   # sourcer le venv à la racine du repo devfest2025-La-Guerre-des-Prompts-attaques-et-defenses-au-royaume-des-LLM/.venv
   source ../../../.venv/bin/activate
   
   # Activate it
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies** (fix for pydantic-core error):
   ```bash
   # Upgrade pip first
   uv pip install --upgrade pip
   
   # Install dependencies with specific Python version compatibility
   uv pip install -r requirements.txt --no-cache-dir

   # Install nemoguardrails
   uv pip install "nemoguardrails[openai]"
   
   # If pydantic-core error persists, try:
   uv pip install pydantic==2.5.0 pydantic-core==2.12.0
   ```

4. **Set environment variables**:
   ```bash
   export NEMO_GUARDRAILS_URL=http://localhost:8001
   export BOT_API_URL=http://localhost:8080
   ```

5. **Run the application locally**:
   ```bash
   # Development mode with auto-reload
   uv run uvicorn app:app --host 0.0.0.0 --port 8002 --reload
   ```

### Running Tests

1. **Fix import errors in tests**:
   The test file has import issues. Check which functions are available:
   ```bash
   # Check available functions in app.py
   python -c "from app import *; print([name for name in dir() if not name.startswith('_')])"
   ```

2. **Run tests**:
   ```bash
   # Run all tests
   python -m pytest tests/ -v
   
   # Run specific test file
   python -m pytest tests/test_jailbreak_detection.py -v
   
   # Run with coverage
   python -m pytest tests/ --cov=. --cov-report=html
   ```

### Docker Development

1. **Build and run with Docker**:
   ```bash
   # Build the image
   docker build -t nemo-proxy ./nemo-proxy
   
   # Run container
   docker run -p 8002:8002 \
     -e NEMO_GUARDRAILS_URL=http://host.docker.internal:8001 \
     -e BOT_API_URL=http://host.docker.internal:8080 \
     nemo-proxy
   ```

## 🔧 Configuration

### Environment Variables
Key environment variables you can customize in your `.env` file:

```bash
# Platform and Tags
PLATFORM=""                    # Docker registry prefix
TAG=25.3.1-amd64               # TOCK version tag
MONGO=8.0.6-amd64              # MongoDB version
POSTGRES_TAG=pg17-amd64        # PostgreSQL version
LANGFUSE_TAG=2.95.8-amd64      # Langfuse version

# External Services
OLLAMA_SERVER=host-gateway     # Ollama server location
GPU_SERVER=192.168.20.2        # GPU server for reranker
OPENAI_API_KEY=your-key-here   # Required for NeMo Guardrails

# Feature Flags
TELEMETRY_ENABLED=true
LANGFUSE_ENABLE_EXPERIMENTAL_FEATURES=false
```

### NeMo Guardrails Configuration
Customize guardrails behavior by editing:
- `nemo-guardrails-config/default/config.yml`
- `nemo-guardrails-config/default/rails.co`
- `nemo-guardrails-config/default/actions.py`

## 🐛 Troubleshooting

### Common Issues

1. **Pydantic-core build error**:
   ```bash
   # Solution: Use compatible versions
   pip install pydantic==2.5.0 pydantic-core==2.12.0
   ```

2. **High disk watermark exceeded**:
    - Ensure you have at least 40GB free space
    - Clean up Docker images/containers: `docker system prune -a`

3. **MongoDB replica set not ready**:
   ```bash
   # Check MongoDB setup
   docker-compose -f docker-compose-genai.yml logs mongo-setup
   
   # Restart if needed
   docker-compose -f docker-compose-genai.yml restart mongo-setup
   ```

4. **Services not accessible**:
   ```bash
   # Check if all services are running
   docker-compose -f docker-compose-genai.yml ps
   
   # Check network connectivity
   docker network ls
   ```

### Debugging Commands

```bash
# View logs for all services
docker-compose -f docker-compose-genai.yml logs

# Follow logs for specific service
docker-compose -f docker-compose-genai.yml logs -f admin_web

# Restart specific service
docker-compose -f docker-compose-genai.yml restart nemo-proxy

# Access container shell
docker-compose -f docker-compose-genai.yml exec nemo-proxy bash
```

## 🛑 Stopping Services

```bash
# Stop all services
docker-compose -f docker-compose-genai.yml down

# Stop and remove volumes (WARNING: This will delete all data)
docker-compose -f docker-compose-genai.yml down -v

# Stop and remove images
docker-compose -f docker-compose-genai.yml down --rmi all
```

## 📚 Additional Resources

- [TOCK Documentation](https://doc.tock.ai/)
- [NeMo Guardrails Documentation](https://github.com/NVIDIA/NeMo-Guardrails)
- [Langfuse Documentation](https://langfuse.com/docs)
- [DevFest 2025 Workshop Materials](../README.md)

## 🤝 Contributing

When contributing to the NeMo Proxy service:
1. Follow the modular architecture in place
2. Add tests for new security features
3. Update this README for configuration changes
4. Test with both local and Docker environments

## ⚠️ Security Notes

- Change default passwords in production
- Secure your OpenAI API key
- Review NeMo Guardrails configuration for your use case
- Monitor Langfuse for prompt injection attempts
- Keep services updated to latest versions