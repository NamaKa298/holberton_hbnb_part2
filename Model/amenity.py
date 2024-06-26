from Model.BaseModel import BaseModel

class Amenity(BaseModel):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(1024), nullable=True)
    place_amenities = db.relationship("Place", secondary="place_amenity")
