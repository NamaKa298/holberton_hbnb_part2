from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from API.v1.auth import auth as auth_blueprint
from config import DevelopmentConfig, ProductionConfig, TestingConfig, Config
import os


app = Flask(__name__)

if os.getenv('ENV') == 'development':
    app.config.from_object(DevelopmentConfig)
elif os.getenv('ENV') == 'testing':
    app.config.from_object(TestingConfig) 
else:
    app.config.from_object(ProductionConfig)

app.config['JWT_SECRET_KEY'] = 'motdepasse'
app.config.from_object(Config)
app.register_blueprint(auth_blueprint, url_prefix='/auth')
db = SQLAlchemy(app)
jwt = JWTManager(app)
