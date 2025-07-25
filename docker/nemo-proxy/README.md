# NeMo Guardrails Proxy

A secure proxy service that applies NeMo Guardrails filtering before forwarding requests to a bot API. This service provides multiple layers of security including input sanitization, jailbreak detection, and content filtering.

## 🏗️ Architecture

The application uses a modular architecture with the following components:

```
nemo-proxy/
├── app.py                     # Main FastAPI application
├── config/
│   └── settings.py           # Configuration settings
├── security/
│   ├── patterns.py           # Security patterns and regex
│   ├── sanitizer.py          # Input/output sanitization
│   └── jailbreak_detector.py # Jailbreak detection logic
├── services/
│   └── __init__.py           # External API communication
├── utils/
│   └── responses.py          # Response utilities
└── tests/
    ├── demo_security.py      # Security demonstration
    ├── test_jailbreak_detection.py
    └── test_security_functions.py
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip
- Docker (optional)
- Docker Compose (optional)

## 📦 Local Development

### 1. Environment Setup

```bash
# Navigate to the project directory
cd docker/nemo-proxy

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Environment Variables

Create a `.env` file in the `nemo-proxy` directory:

```bash
# Required services
NEMO_GUARDRAILS_URL=http://localhost:8000
BOT_API_URL=http://localhost:8080

# Optional settings
LOG_LEVEL=DEBUG
```

### 3. Run the Application

```bash
# Run with Python directly
python app.py

# Or run with uvicorn for development
uvicorn app:app --host 0.0.0.0 --port 8001 --reload
```

The application will be available at `http://localhost:8001`

### 4. API Endpoints

- **Health Check**: `GET /health`
- **Root**: `GET /`
- **Main Proxy**: `POST /io/app/new_assistant/web`

Example request:
```bash
curl -X POST http://localhost:8001/io/app/new_assistant/web \
  -H "Content-Type: application/json" \
  -d '{"query": "Hello, how are you?"}'
```

## 🐳 Docker Deployment

### 1. Build Docker Image

```bash
# From the nemo-proxy directory
docker build -t nemo-proxy:latest .
```

### 2. Run with Docker

```bash
# Run single container
docker run -p 8001:8001 \
  -e NEMO_GUARDRAILS_URL=http://nemo-guardrails:8000 \
  -e BOT_API_URL=http://bot_api:8080 \
  nemo-proxy:latest
```

### 3. Run with Docker Compose

From the main project directory:

```bash
# Start all services
docker-compose -f docker/docker-compose-genai.yml up -d

# Check logs
docker-compose -f docker/docker-compose-genai.yml logs nemo-proxy

# Stop services
docker-compose -f docker/docker-compose-genai.yml down
```

## 🧪 Testing

### 1. Run Unit Tests

```bash
# From the nemo-proxy directory
cd docker/nemo-proxy

# Run all tests
python -m pytest tests/ -v

# Run specific test files
python -m pytest tests/test_jailbreak_detection.py -v
python -m pytest tests/test_security_functions.py -v

# Run with coverage
python -m pytest tests/ --cov=. --cov-report=html
```

### 2. Run Security Demonstration

```bash
# Interactive security demo
python tests/demo_security.py
```

### 3. Integration Tests

```bash
# Test with live services (requires services to be running)
# From the main docker directory
./test-guardrails.sh

# Test NeMo Guardrails directly
python test_guardrails.py
```

## 🔧 Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `NEMO_GUARDRAILS_URL` | `http://nemo-guardrails:8000` | NeMo Guardrails service URL |
| `BOT_API_URL` | `http://bot_api:8080` | Bot API service URL |
| `LOG_LEVEL` | `DEBUG` | Logging level (DEBUG, INFO, WARNING, ERROR) |

### Security Settings

The application includes multiple security layers:

1. **Input Sanitization**: HTML escaping, length limits, dangerous pattern detection
2. **Jailbreak Detection**: Regex-based pattern matching for prompt injection attempts
3. **NeMo Guardrails**: AI-based content filtering
4. **Output Sanitization**: XSS prevention and content filtering

## 📊 Monitoring and Logs

### View Logs

```bash
# Local development
tail -f logs/app.log

# Docker
docker logs -f nemo-proxy

# Docker Compose
docker-compose -f docker/docker-compose-genai.yml logs -f nemo-proxy
```

### Health Monitoring

```bash
# Check service health
curl http://localhost:8001/health

# Expected response
{
  "status": "healthy",
  "service": "nemo-proxy"
}
```

## 🛠️ Development

### Adding New Security Patterns

1. Add patterns to `security/patterns.py`
2. Update tests in `tests/test_jailbreak_detection.py`
3. Run tests to verify

### Modifying Services

1. Update service classes in `services/__init__.py`
2. Add corresponding tests
3. Update configuration if needed

### Code Quality

```bash
# Format code
black .

# Lint code
flake8 .

# Type checking
mypy .
```

## 🚨 Troubleshooting

### Common Issues

1. **Service Unavailable Errors**
   - Check if NeMo Guardrails and Bot API services are running
   - Verify environment variables are set correctly

2. **Import Errors**
   - Ensure you're in the correct directory
   - Check virtual environment is activated
   - Verify dependencies are installed

3. **Port Conflicts**
   - Change port in `app.py` or use different port with uvicorn
   - Check for other services using the same port

### Debug Mode

```bash
# Run with debug logging
LOG_LEVEL=DEBUG python app.py

# Run with uvicorn debug mode
uvicorn app:app --host 0.0.0.0 --port 8001 --reload --log-level debug
```

## 📝 API Documentation

Once the application is running, visit:
- Swagger UI: `http://localhost:8001/docs`
- ReDoc: `http://localhost:8001/redoc`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## 📄 License

This project is part of the DevFest 2025 workshop on LLM security.
