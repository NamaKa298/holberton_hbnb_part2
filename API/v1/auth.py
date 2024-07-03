from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

auth = Blueprint('auth', __name__)
auth_blueprint = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    from Model.user import User
    
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    if not email or not password:
        return jsonify({"msg": "Email and password are required"}), 400
    try:
        user = User.find_by_email(email)
        print(user.password)
        if user and User.check_password(user, password):
            additional_claims = {"is_admin": user.is_admin}
            access_token = create_access_token(identity=user.id, additional_claims=additional_claims)
            return jsonify(access_token=access_token), 200
        else:
            return jsonify({"msg": "Invalid email or password"}), 401
    except Exception as e:
        print(e)
        return jsonify({"msg": "An error occurred"}), 500

# @auth_blueprint.route('/login', methods=['POST'])
# def login():
#     from Model.user import User
#     username = request.json.get('username', None)
#     password = request.json.get('password', None)
#     user = User.authenticate(username, password)
#     if user:
#         # Inclure le rôle de l'utilisateur dans le token
#         access_token = create_access_token(identity=username, additional_claims={"role": user.role})
#         return jsonify(access_token=access_token), 200
#     else:
#         return jsonify({"msg": "Bad username or password"}), 401
