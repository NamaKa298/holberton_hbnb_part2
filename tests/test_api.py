import pytest
from flask import Flask, json
from api_00 import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_user(client):
    response = client.post('/users', json={'name': 'John', 'email': 'john@example.com'})
    assert response.status_code == 201
    assert response.get_json()['name'] == 'John'
    assert response.get_json()['email'] == 'john@example.com'
