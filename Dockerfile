# Utilise une image Python officielle légère
FROM python:3.11-slim

# Variables d'environnement pour éviter buffers en Python
ENV PYTHONUNBUFFERED=1

# Dossier de travail dans le container
WORKDIR /app

# Copier requirements + installer dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le projet dans le container
COPY . .

# Création dossier base SQLite (pour persistance)
RUN mkdir -p db

# Commande par défaut à l’exécution
CMD ["python", "run_project.py"]FROM python:3.11-slim

WORKDIR /app

# Installer dépendances système
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copier fichiers requirements.txt
COPY requirements.txt .

# Installer dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source
COPY . .

CMD ["python", "analyser_donnees.py"]