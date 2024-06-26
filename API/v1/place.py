from flask import request, jsonify
from API.v1.app import app
from Persistence.datamanager import data_manager as place_repository
from Model.place import Place

@app.route('/places', methods=['POST'])
def create_place():
    data = request.get_json()
    place = Place(**data)
    place_repository.save(place)
    return jsonify(place.to_dict()), 201

@app.route('/places', methods=['GET'])
def read_places():
    places = place_repository.all("Place")
    return jsonify([places[id].to_dict() for id in places]), 200

@app.route('/places/<id>', methods=['GET'])
def read_place(id):
    place = place_repository.get(id, "Place")
    if place is None:
        return jsonify({"error": "Place not found"}), 404
    return jsonify(place.to_dict()), 200

@app.route('/places/<id>', methods=['PUT'])
def update_place(id):
    place = place_repository.get(id, "Place")
    if place is None:
        return jsonify({"error": "Place not found"}), 404
    data = request.get_json()
    place_repository.update(place, **data)
    return jsonify(place.to_dict()), 200

@app.route('/places/<id>', methods=['DELETE'])
def delete_place(id):
    place = place_repository.get(id, "Place")
    if place is None:
        return jsonify({"error": "Place not found"}), 404
    place_repository.delete(place, "Place")
    return jsonify({}), 204

