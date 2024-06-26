from Model.BaseModel import BaseModel
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Review(BaseModel):
    __tablename__ = 'reviews'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    text = db.Column(db.String(1024), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    place_id = db.Column(db.String(36), db.ForeignKey('place.id'), nullable=False)

    user = db.relationship('User', backref=db.backref('reviews', lazy=True))
    place = db.relationship('Place', backref=db.backref('reviews', lazy=True))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
