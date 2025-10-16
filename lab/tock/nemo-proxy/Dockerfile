FROM python:3.12-slim-bookworm

WORKDIR /app

# Install system dependencies for C++ bindings (annoy, etc.)
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc g++ python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements.txt first to leverage Docker cache
COPY requirements.txt .

# Update pip and install Python dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# Install NeMo Guardrails with 'openai' extra to support OpenAI-based moderation
RUN pip install nemoguardrails[openai]

# Copy application source code
COPY . .

# Expose port used by FastAPI/Uvicorn
EXPOSE 8002

# Command to launch FastAPI application with Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8002"]
