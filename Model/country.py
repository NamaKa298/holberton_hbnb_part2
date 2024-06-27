from Model.BaseModel import BaseModel
from sqlalchemy import Column, String, Integer
from uuid import uuid4

class Country(BaseModel):
    __tablename__ = 'countries'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    name = Column(String(100), nullable=False)
    population = Column(Integer)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
