from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt
from API.v1.app import app, db

admin_blueprint = Blueprint('admin', __name__)
@admin_blueprint.route('/admin/data', methods=['POST', 'DELETE'])
@jwt_required()
def admin_data():
    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({"msg": "Administration rights required"}), 403
    # Procéder avec la fonctionnalité réservée aux administrateurs
    return jsonify({"msg": "Admin data processed"}), 200

app.register_blueprint(admin_blueprint)

@admin_blueprint.route('/change_role/<user_id>', methods=['PUT'])
@jwt_required()
def change_user_role(user_id):
    from Model.user import User
    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({"msg": "Administration rights required"}), 403
    new_role = request.json.get('role', None)
    user = User.query.get(user_id)
    if user:
        user.role = new_role
        db.session.commit()
        return jsonify({"msg": "User role updated"}), 200
    else:
        return jsonify({"msg": "User not found"}), 404
