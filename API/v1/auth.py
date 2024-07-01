from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

auth = Blueprint('auth', __name__)
auth_blueprint = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    from Model.user import User
    
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    if not email or not password:
        return jsonify({"msg": "Email and password are required"}), 400

    user = User.find_by_email(email)
    if user and check_password_hash(user.password, password):
        additional_claims = {"is_admin": user.is_admin}
        access_token = create_access_token(identity=user.id, additional_claims=additional_claims)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Invalid email or password"}), 401

@auth_blueprint.route('/login', methods=['POST'])
def login():
    from Model.user import User
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    user = User.authenticate(username, password)
    if user:
        # Inclure le rôle de l'utilisateur dans le token
        access_token = create_access_token(identity=username, additional_claims={"role": user.role})
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Bad username or password"}), 401
