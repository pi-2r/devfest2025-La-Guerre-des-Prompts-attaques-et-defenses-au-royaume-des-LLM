FROM python:3.9

WORKDIR /app

# Installer les dépendances système pour les bindings C++ (annoy, etc.)
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc g++ python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Copier requirements.txt avant pour bénéficier du cache Docker
COPY requirements.txt .

# Mettre à jour pip et installer les dépendances Python
RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# Installer NeMo Guardrails avec l'extra 'openai' pour supporter la modération basée sur OpenAI
#RUN pip install --no-cache-dir "nemoguardrails[openai]="
RUN pip install nemoguardrails[openai]

# Copier le code source de l'application
COPY . .

# Exposer le port utilisé par FastAPI/Uvicorn
EXPOSE 8002

# Commande pour lancer l'application FastAPI avec Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8002"]
