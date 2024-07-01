import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

db = None
Base = None

if (os.getenv('ENV') == 'testing'):
    db = SQLAlchemy()
    Base = db.Model
else:
    from API.v1.app import app
    db = SQLAlchemy(app)
    Base = db.Model

metadata = db.metadata
