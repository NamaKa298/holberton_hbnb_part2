# Utiliser l'image officielle d'Alpine Linux avec Python 3.8
FROM python:3.8-alpine
# Installer les dépendances nécessaires pour PostgreSQL
# gcc et python3-dev sont nécessaires pour compiler certaines dépendances Python
# postgresql-dev est nécessaire pour PostgreSQL
RUN apk add --no-cache postgresql-dev gcc python3-dev
# Copier le reste du code de l'application dans le conteneur
COPY . /app
# Définir le répertoire de travail dans le conteneur
WORKDIR /app
# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt
# Exposer le port 5000
EXPOSE 5000
# Configurer Gunicorn pour utiliser le port 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
