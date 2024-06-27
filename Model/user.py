from Model.BaseModel import BaseModel
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from uuid import uuid4
import re

class User(BaseModel):
    __tablename__ = 'users'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    is_admin = Column(Boolean, default=False)

    # places = relationship('Place', backref='users', lazy=True)
    # reviews = relationship('Review', backref='users', lazy=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def is_valid_email(email):
        """Check if email is valid"""
        return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))
