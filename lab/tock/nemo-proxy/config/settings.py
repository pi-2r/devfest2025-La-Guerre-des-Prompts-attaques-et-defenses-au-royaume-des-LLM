"""
Configuration settings for the NeMo Proxy application
"""
import os

# Service URLs
NEMO_GUARDRAILS_URL = os.getenv("NEMO_GUARDRAILS_URL", "http://nemo-guardrails:8000")
BOT_API_URL = os.getenv("BOT_API_URL", "http://bot_api:8080")  # Corriger l'URL pour Docker

# Security settings
MAX_INPUT_LENGTH = 10000
ALLOWED_HTML_TAGS = ['p', 'br', 'strong', 'em', 'ul', 'ol', 'li']
ALLOWED_HTML_ATTRIBUTES = {}

# Logging configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# CORS settings
CORS_ORIGINS = ["*"]  # Should be restricted in production
CORS_METHODS = ["GET", "POST", "OPTIONS"]
CORS_HEADERS = ["*"]

# Optimized NeMo Guardrails settings
USE_DIRECT_GUARDRAILS = os.getenv("USE_DIRECT_GUARDRAILS", "true").lower() == "true"
# Utiliser le chemin vers la configuration montée dans le conteneur Docker
GUARDRAILS_CONFIG_PATH = os.getenv("GUARDRAILS_CONFIG_PATH", "/app/nemo-guardrails-config")
