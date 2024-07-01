from datetime import datetime
from typing import TypeVar, List, Dict
from Persistence.interface_persistence import IPersistenceManager
from flask_sqlalchemy import SQLAlchemy
from API.v1.app import db, app
import os
import json

class DataManager(IPersistenceManager):

    def __init__(self):
        import Model
        self.classes = {
            "Amenity": Model.Amenity,
            "City": Model.City,
            "Country": Model.Country,
            "Place": Model.Place,
            "Review": Model.Review,
            "User": Model.User,
        }
        self._loaded = True
        self.storage = {}  # For the sake of simplicity, we'll use a dictionary as our storage

        # Check configuration for database usage
        self.use_database = os.getenv('USE_DATABASE', False)

        # Initialize based on configuration
        if self.use_database:
            self.__load_all_from_db()
        else:
            self.__load_all_from_file()

    async def loaded(self):
        return self._loaded

    def __load_all_from_db(self):
        with app.app_context():
            db.create_all()
            for entity_name, entity_class in self.classes.items():
                entities = db.session.query(entity_class).all()
                self.storage[entity_name] = {entity.id: entity for entity in entities}

    def __load_all_from_file(self):
        data = self.read_database()
        for entity_type in data:
            self.storage[entity_type] = {}
            for entity_id in data[entity_type]:
                clazz = self.classes[entity_type]
                entity_data = data[entity_type][entity_id]
                entity = clazz(**entity_data)
                self.storage[entity_type][entity_id] = entity
    
    def read_database(self, database_name=None):
        database_path = f'Persistence/{database_name}.json' if database_name else 'Persistence/database.json'
        try:
            with open(database_path, 'r') as file:
                return json.load(file)
        except Exception:
            return {}

    def all(self, entity_type=None):
        if entity_type is None:
            return self.storage
        return self.storage.get(entity_type, {})

    def save(self, entity):
        entity_type = type(entity).__name__
        if entity_type not in self.storage:
            self.storage[entity_type] = {}
        self.storage[entity_type][entity.id] = entity
        if self.use_database:
            db.session.add(entity)
            db.session.commit()
        else:
            self.save_all()

    def save_all(self):
        if not self.use_database:
            with open('Persistence/database.json', 'w') as file:
                data = {}
                for entity_type in self.storage:
                    data[entity_type] = {}
                    for entity_id in self.storage[entity_type]:
                        data[entity_type][entity_id] = self.storage[entity_type][entity_id].to_dict()
                json.dump(data, file)

    def get(self, entity_id, entity_type):
        if self.use_database:
            return self.storage.get(entity_type, {}).get(entity_id, None)
        else:
            return self.storage.get(entity_type, {}).get(entity_id, None)

    def update(self, entity, **kwargs):
        if self.use_database:
            for key in kwargs:
                setattr(entity, key, kwargs[key])
            entity.updated_at = datetime.now()
            db.session.commit()
        else:
            if (kwargs):
                for key in kwargs:
                    setattr(entity, key, kwargs[key])
                entity.updated_at = datetime.now()
                self.save_all()

    def delete(self, entity, entity_type):
        if self.use_database:
            if entity_type in self.storage and entity.id in self.storage[entity_type]:
                del self.storage[entity_type][entity.id]
                db.session.delete(entity)
                db.session.commit()
        else:
            if entity_type in self.storage and entity.id in self.storage[entity_type]:
                del self.storage[entity_type][entity.id]
                self.save_all()

