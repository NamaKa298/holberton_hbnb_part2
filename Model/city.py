from Model.BaseModel import BaseModel
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class City(BaseModel):
    __tablename__ = 'cities'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    population = db.Column(db.Integer)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
