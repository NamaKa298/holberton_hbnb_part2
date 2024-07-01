from .BaseModel import BaseModel
from sqlalchemy import Column, String

class Amenity(BaseModel):
    __tablename__ = 'amenities'

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
