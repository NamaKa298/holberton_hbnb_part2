from sqlalchemy import Column, String, DateTime
from engine.database import Base
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid

data = {}

class BaseModel(Base):
    """Represent the base class for all models in the application"""

    __abstract__ = True

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, **kwargs):
        """Initialize a new instance of the BaseModel class"""
        super().__init__()
        for key, value in kwargs.items():
            if hasattr(self, key):
                if key in ["created_at", "updated_at"] and isinstance(value, str):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)

    
    @classmethod
    def exists(cls, entity):
        # Assuming 'data' is a global or accessible dictionary holding entities
        cls_entities = data.get(cls.__name__)
        return (
            True if cls_entities 
            and cls_entities.get(entity.id) 
            else False
        )

    def to_dict(self):
        """Return a dictionary representation of the instance for JSON serialization."""
        data = {}
        for key, value in self.__dict__.items():
            if key.startswith('_'):
                continue  # Skip internal attributes
            if isinstance(value, datetime):
                data[key] = value.isoformat()
            else:
                data[key] = value
        return data