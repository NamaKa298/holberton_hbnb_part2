from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig, ProductionConfig, TestingConfig
import os

app = Flask(__name__)

if os.getenv('ENV') == 'development':
    app.config.from_object(DevelopmentConfig)
elif os.getenv('ENV') == 'testing':
    app.config.from_object(TestingConfig) 
else:
    app.config.from_object(ProductionConfig)

db = SQLAlchemy(app)

@app.before_first_request
def initialize_database():
    """Crée toutes les tables définies dans les modèles si elles n'existent pas."""
    db.create_all()

if __name__ == '__main__':
    app.run()
