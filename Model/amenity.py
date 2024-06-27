from Model.BaseModel import BaseModel
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Amenity(BaseModel):
    __tablename__ = 'amenities'

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
