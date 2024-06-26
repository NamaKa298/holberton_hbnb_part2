from Model.BaseModel import BaseModel
from flask_sqlalchemy import SQLAlchemy
import re

db = SQLAlchemy()

class User(BaseModel):
    __tablename__ = 'users'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    places = db.relationship('Place', backref='user', lazy=True)
    reviews = db.relationship('Review', backref='user', lazy=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def is_valid_email(email):
        """Check if email is valid"""
        return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))
