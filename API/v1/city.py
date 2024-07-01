from flask import request, jsonify
from API.v1.app import app
from Model.city import City
from flask_jwt_extended import jwt_required, get_jwt

@app.route('/cities', methods=['POST'])
@jwt_required()
def create_city():
    from Persistence import data_manager as city_repository
    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({"msg": "Administration rights required"}), 403
    all_cities = city_repository.all("City")
    data = request.get_json()
    for id in all_cities:
        current_city = all_cities[id]
        has_same_name = current_city.name == data["name"]
        has_same_country_code = current_city.country_code == data["country_code"]
        if has_same_name and has_same_country_code:
            return jsonify({"error": "City already exist in this country"}), 404  
    city = City(**data)
    city_repository.save(city)
    return jsonify(city.to_dict()), 201

@app.route('/cities', methods=['GET'])
def read_cities():
    from Persistence import data_manager as city_repository
    cities = city_repository.all("City")
    return jsonify([cities[id].to_dict() for id in cities]), 200

@app.route('/cities/<id>', methods=['GET'])
def read_city(id):
    from Persistence import data_manager as city_repository
    city = city_repository.get(id, "City")
    if city is None:
        return jsonify({"error": "City not found"}), 404
    return jsonify(city.to_dict()), 200

@app.route('/cities/<id>', methods=['PUT'])
def update_city(id):
    from Persistence import data_manager as city_repository
    city = city_repository.get(id, "City")
    if city is None:
        return jsonify({"error": "City not found"}), 404
    data = request.get_json()
    city_repository.update(city, **data)
    return jsonify(city.to_dict()), 200

@app.route('/cities/<id>', methods=['DELETE'])
def delete_city(id):
    from Persistence import data_manager as city_repository
    city = city_repository.get(id, "City")
    if city is None:
        return jsonify({"error": "City not found"}), 404
    city_repository.delete(city, "City")
    return jsonify({}), 204
