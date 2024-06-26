from flask import request, jsonify
from API.v1.app import app
from Persistence.datamanager import data_manager as city_repository
from Model.city import City

@app.route('/cities', methods=['POST'])
def create_city():
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
    cities = city_repository.all("City")
    return jsonify([cities[id].to_dict() for id in cities]), 200

@app.route('/cities/<id>', methods=['GET'])
def read_city(id):
    city = city_repository.get(id, "City")
    if city is None:
        return jsonify({"error": "City not found"}), 404
    return jsonify(city.to_dict()), 200

@app.route('/cities/<id>', methods=['PUT'])
def update_city(id):
    city = city_repository.get(id, "City")
    if city is None:
        return jsonify({"error": "City not found"}), 404
    data = request.get_json()
    city_repository.update(city, **data)
    return jsonify(city.to_dict()), 200

@app.route('/cities/<id>', methods=['DELETE'])
def delete_city(id):
    city = city_repository.get(id, "City")
    if city is None:
        return jsonify({"error": "City not found"}), 404
    city_repository.delete(city, "City")
    return jsonify({}), 204
