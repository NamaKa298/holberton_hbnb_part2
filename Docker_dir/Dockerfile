# Utiliser l'image officielle d'Alpine Linux avec Python 3.8
FROM python:3.8-alpine

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt ./

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code de l'application dans le conteneur
COPY . .

# Définir un volume pour la persistance des données
VOLUME /app/data

# Définir la variable d'environnement pour le port
ENV PORT=8000

# Exposer le port défini par la variable d'environnement
EXPOSE $PORT

# Configurer Gunicorn pour utiliser le port défini
CMD ["gunicorn", "-b", "0.0.0.0:$PORT", "wsgi:app"]