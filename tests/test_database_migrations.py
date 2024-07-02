import unittest
import os

os.environ["ENV"] = "testing"

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from alembic import command
from alembic.config import Config
from engine.database import metadata
import Model

class MigrationTest(unittest.TestCase):
    SQLITE_DB_URI = "sqlite:///test.db"
    POSTGRESQL_DB_URI = "postgresql://user:password@localhost/testdb"

    def setUp(self):
        # Choose the database URI based on the test environment
        self.db_uri = self.SQLITE_DB_URI if self._testMethodName.startswith("test_dev_") else self.POSTGRESQL_DB_URI
        self.engine = create_engine(self.db_uri)
        self.session = sessionmaker()(bind=self.engine)
        metadata.create_all(self.engine)

    def tearDown(self):
        self.engine.dispose()

    def run_alembic_migrations(self):
        alembic_cfg = Config("alembic.ini")
        alembic_cfg.set_main_option("sqlalchemy.url", self.db_uri)
        command.upgrade(alembic_cfg, "head")

    def test_dev_keep_data(self):
        """populate the database with some data before running the migrations"""
        my_user = Model.User(email="lemaildebenoit", password="lepassword")
        self.session.add(my_user)
        self.session.commit()
        user_id = my_user.id
        my_place = Model.Place(name="Paris", description="la ville de l'amour", user_id=user_id)
        self.session.add(my_place)
        self.session.commit()
        place_id = my_place.id
        amenity = Model.Amenity(name="wifi", description="internet")
        self.session.add(amenity)
        self.session.commit()
        city = Model.City(name="Paris", population=1000000)
        self.session.add(city)
        self.session.commit()
        country = Model.Country(name="France", population=100000000)
        self.session.add(country)
        self.session.commit()
        review = Model.Review(text="super", place_id=place_id, user_id=user_id)
        self.session.add(review)
        self.session.commit()

    def test_dev_sqlite_migration(self):
        """Test migrations on SQLite (Development environment)"""
        try:
            self.run_alembic_migrations()
        except SQLAlchemyError as e:
            self.fail(f"SQLite migration failed: {e}")

    def test_dev_migration_with_rollback(self):
        alembic_cfg = Config("alembic.ini")
        alembic_cfg.set_main_option("sqlalchemy.url", self.db_uri)
   
        try:
            command.upgrade(alembic_cfg, "head")
            command.downgrade(alembic_cfg, "-1")
            command.upgrade(alembic_cfg, "base")
        
        except Exception as e:
           self.fail(f"Migration with rollback failed: {e}")


if __name__ == '__main__':
    unittest.main()
