# Utiliser une image de base légère, par exemple Python 3.8 Alpine
FROM python:3.8-alpine
ENV PYTHONPATH=/app
# Copier le reste du code de l'application dans le conteneur
COPY . /app

# Exposer le port sur lequel l'application va tourner
EXPOSE 5000

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier uniquement le fichier requirements.txt au début pour profiter du caching des couches Docker
COPY requirements.txt /app/

# Installer les dépendances nécessaires pour MySQL, gcc et python3-dev sont nécessaires pour compiler certaines dépendances Python
# Il est important de nettoyer après l'installation pour garder l'image légère
RUN apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .build-deps

# Configurer Gunicorn pour lancer l'application
CMD ["gunicorn", "-b", "0.0.0.0:5000", "--timeout", "120", "wsgi:app"]
