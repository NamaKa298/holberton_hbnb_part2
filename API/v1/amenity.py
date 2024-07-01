from flask_jwt_extended import jwt_required, get_jwt
from flask import jsonify, request
from API.v1.app import app
from Model.amenity import Amenity

@app.route('/amenities', methods=['POST'])
@jwt_required()
def create_amenity():
    from Persistence import data_manager as amenity_repository
    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({"msg": "Administration rights required"}), 403
    data = request.get_json()
    amenity = Amenity(**data)
    amenity_repository.save(amenity)
    return jsonify(amenity.to_dict()), 201

@app.route('/amenities', methods=['GET'])
def read_amenities():
    from Persistence import data_manager as amenity_repository
    amenities = amenity_repository.all("Amenity")
    return jsonify([amenities[id].to_dict() for id in amenities]), 200

@app.route('/amenities/<id>', methods=['GET'])
def read_amenity(id):
    from Persistence import data_manager as amenity_repository
    amenity = amenity_repository.get(id, "Amenity")
    if amenity is None:
        return jsonify({"error": "Amenity not found"}), 404
    return jsonify(amenity.to_dict()), 200

@app.route('/amenities/<id>', methods=['PUT'])
def update_amenity(id):
    from Persistence import data_manager as amenity_repository
    amenity = amenity_repository.get(id, "Amenity")
    if amenity is None:
        return jsonify({"error": "Amenity not found"}), 404
    data = request.get_json()
    amenity_repository.update(amenity, **data)
    return jsonify(amenity.to_dict()), 200

@app.route('/amenities/<id>', methods=['DELETE'])
def delete_amenity(id):
    from Persistence import data_manager as amenity_repository
    amenity = amenity_repository.get(id, "Amenity")
    if amenity is None:
        return jsonify({"error": "Amenity not found"}), 404
    amenity_repository.delete(amenity, "Amenity")
    return jsonify({}), 204

