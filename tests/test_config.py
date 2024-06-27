import os
import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app, db
from config import DevelopmentConfig, ProductionConfig, TestingConfig

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_development_config():
    os.environ['ENV'] = 'development'
    app.config.from_object(DevelopmentConfig)
    assert app.config['DEBUG'] is True
    assert app.config['SQLALCHEMY_DATABASE_URI'] == DevelopmentConfig.SQLALCHEMY_DATABASE_URI

def test_testing_config():
    os.environ['ENV'] = 'testing'
    app.config.from_object(TestingConfig)
    assert app.config['TESTING'] is True
    assert app.config['SQLALCHEMY_DATABASE_URI'] == TestingConfig.SQLALCHEMY_DATABASE_URI

def test_production_config():
    os.environ['ENV'] = 'production'
    app.config.from_object(ProductionConfig)
    assert app.config['DEBUG'] is False
    assert app.config['SQLALCHEMY_DATABASE_URI'] == ProductionConfig.SQLALCHEMY_DATABASE_URI

def test_default_config():
    if 'ENV' in os.environ:
        del os.environ['ENV']
    app.config.from_object(ProductionConfig)  # Assuming ProductionConfig is the default
    assert app.config['DEBUG'] is False
    assert app.config['SQLALCHEMY_DATABASE_URI'] == ProductionConfig.SQLALCHEMY_DATABASE_URI

def test_sqlalchemy_initialization():
    assert isinstance(db, SQLAlchemy)
