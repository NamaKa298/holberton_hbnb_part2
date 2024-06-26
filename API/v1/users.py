from flask import request, jsonify
from API.v1.app import app
from Persistence.datamanager import data_manager as user_repository
from Model.user import User

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(**data)
    user_repository.save(user)
    return jsonify(user.to_dict()), 201

@app.route('/users', methods=['GET'])
def read_users():
    users = user_repository.all("User")
    return jsonify([users[id].to_dict() for id in users]), 200

@app.route('/users/<id>', methods=['GET'])
def read_user(id):
    user = user_repository.get(id, "User")
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict()), 200

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    user = user_repository.get(id, "User")
    if user is None:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    user_repository.update(user, **data)
    return jsonify(user.to_dict()), 200

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    user = user_repository.get(id, "User")
    if user is None:
        return jsonify({"error": "User not found"}), 404
    user_repository.delete(user, "User")
    return jsonify({}), 204
