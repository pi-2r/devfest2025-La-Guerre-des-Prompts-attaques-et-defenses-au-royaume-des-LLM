FROM python:3.9

WORKDIR /app

# Copy requirements first to leverage Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Install core dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Install langchain and langchain-community
RUN pip install -U langchain langchain-community

COPY install_nemoguardrails.sh .
RUN chmod +x install_nemoguardrails.sh && ./install_nemoguardrails.sh


# Copy application code
COPY . .

# Expose port
EXPOSE 8002

# Run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8002"]
