from Model.BaseModel import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import backref, relationship
from uuid import uuid4

class Place(BaseModel):
    __tablename__ = 'places'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    user = relationship('User', backref=backref('places', lazy=True))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.amenities = []
        self.reviews = []  # Prepare a list for associated reviews at startup
