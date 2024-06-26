from Model.BaseModel import BaseModel

class Country():
    def __init__(self, *args, **kwargs):
        if (kwargs):
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        
        if (args):
            for key, value in args.items():
                setattr(self, key, value)
