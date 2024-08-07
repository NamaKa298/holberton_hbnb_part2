from flask import request, jsonify
from API.v1.app import app
from Model.user import User
import logging

@app.route('/users', methods=['POST'])
def create_user():
    from Persistence import data_manager as user_repository
    try:
        data = request.get_json()
        user = User(**data)
        user.set_password(data["password"])
        user_repository.save(user)
        return jsonify({
            "id": user.id,
            "email": user.email,
            "password": user.password,
            "is_admin": user.is_admin,
            "created_at": user.created_at,
            "updated_at": user.updated_at
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/users', methods=['GET'])
def read_users():
    from Persistence import data_manager as user_repository
    users = user_repository.all("User")
    return jsonify([users[id].to_dict() for id in users]), 200

@app.route('/users/<id>', methods=['GET'])
def read_user(id):
    from Persistence import data_manager as user_repository
    user = user_repository.get(id, "User")
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict()), 200

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    from Persistence import data_manager as user_repository
    user = user_repository.get(id, "User")
    if user is None:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    user_repository.update(user, **data)
    return jsonify(user.to_dict()), 200

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    from Persistence import data_manager as user_repository
    user = user_repository.get(id, "User")
    if user is None:
        return jsonify({"error": "User not found"}), 404
    user_repository.delete(user, "User")
    return jsonify({}), 204
