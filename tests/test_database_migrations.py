import unittest
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from alembic import command
from alembic.config import Config

class MigrationTest(unittest.TestCase):
    SQLITE_DB_URI = "sqlite:///:memory:"
    POSTGRESQL_DB_URI = "postgresql://user:password@localhost/testdb"

    def setUp(self):
        # Choose the database URI based on the test environment
        self.db_uri = self.SQLITE_DB_URI if self._testMethodName.startswith("test_dev_") else self.POSTGRESQL_DB_URI
        self.engine = create_engine(self.db_uri)
        self.Session = sessionmaker(bind=self.engine)

    def tearDown(self):
        self.engine.dispose()

    def run_alembic_migrations(self):
        alembic_cfg = Config("alembic.ini")
        alembic_cfg.set_main_option("sqlalchemy.url", self.db_uri)
        command.upgrade(alembic_cfg, "head")

    def test_dev_sqlite_migration(self):
        """Test migrations on SQLite (Development environment)"""
        try:
            self.run_alembic_migrations()
        except SQLAlchemyError as e:
            self.fail(f"SQLite migration failed: {e}")

    def test_prod_postgresql_migration(self):
        """Test migrations on PostgreSQL (Production-like environment)"""
        try:
            self.run_alembic_migrations()
        except SQLAlchemyError as e:
            self.fail(f"PostgreSQL migration failed: {e}")

if __name__ == '__main__':
    unittest.main()
