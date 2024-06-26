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

def test_create_user_no_json(client):
    response = client.post('/users')
    assert response.status_code == 400
    assert response.get_json() == {"error": "Not a JSON"}

def test_create_user_no_name(client):
    response = client.post('/users', json={'email': '
    assert response.status_code == 400
    assert response.get_json() == {"error": "Missing name"}

def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert response.get_json() == {"users": []}

def test_get_user(client):
    response = client.get('/users/1')
    assert response.status_code == 200
    assert response.get_json() == {"user_id": 1}

def test_update_user(client):
    response = client.put('/users/1', json={'name': 'John', 'email': '
    assert response.status_code == 200
    assert response.get_json() == {"user_id": 1, "name": 'John', "email": '

def test_update_user_no_json(client):
    response = client.put('/users/1')
    assert response.status_code == 400
    assert response.get_json() == {"error": "Not a JSON"}

def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.status_code == 204
    assert response.get_data(as_text=True) == ''

def test_delete_user_no_json(client):
    response = client.delete('/users/1')
    assert response.status_code == 204
    assert response.get_data(as_text=True) == ''
