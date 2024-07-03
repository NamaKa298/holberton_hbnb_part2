from .BaseModel import BaseModel
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Boolean, Integer
from uuid import uuid4
import re
from bcrypt import checkpw, hashpw, gensalt


class User(BaseModel):
    __tablename__ = 'users'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    is_admin = Column(Boolean, default=False)
    role = Column(String(80), default='user')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def is_valid_email(email):
        """Check if email is valid"""
        return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

    def set_password(self, password):
        bytes = password.encode('utf-8')
        salt = gensalt()
        self.password = hashpw(bytes, salt)

    @staticmethod
    def check_password(user, password):
        bytes = password.encode('utf-8')
        return checkpw(bytes, user.password.encode('utf-8'))

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()