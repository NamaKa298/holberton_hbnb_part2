from Model.BaseModel import BaseModel
from Model.user import User


class Place(BaseModel):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.amenities = []
        self.reviews = [] ### On prépare une liste pour associé les reviews lié à la place au démarrage du programme
