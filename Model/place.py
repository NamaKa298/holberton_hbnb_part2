from Model.BaseModel import BaseModel
from Model.user import User
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Place(BaseModel):
    __tablename__ = 'places'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(1024), nullable=True)
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('places', lazy=True))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.amenities = []
        self.reviews = []  # Prepare a list for associated reviews at startup
