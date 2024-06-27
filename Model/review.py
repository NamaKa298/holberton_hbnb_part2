from Model.BaseModel import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from uuid import uuid4

class Review(BaseModel):
    __tablename__ = 'reviews'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    text = Column(String(1024), nullable=False)
    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    place_id = Column(String(36), ForeignKey('places.id'), nullable=False)

    user = relationship('User', backref=backref('reviews', lazy=True))
    place = relationship('Place', backref=backref('reviews', lazy=True))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
