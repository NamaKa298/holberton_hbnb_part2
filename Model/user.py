from Model.BaseModel import BaseModel
import re

class User(BaseModel):
    
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.places = []
        self.reviews = []
        
    @staticmethod
    def is_valid_email(email):
        """Check if email is valid"""
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return True
        return False