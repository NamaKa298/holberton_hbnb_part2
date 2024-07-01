from flask import request, jsonify, Blueprint
from API.v1.app import app
from Model.place import Place

place_blueprint = Blueprint('place', __name__)

@app.route('/places', methods=['POST'])
def create_place():
    from Persistence import data_manager as place_repository
    data = request.get_json()
    place = Place(**data)
    place_repository.save(place)
    return jsonify(place.to_dict()), 201

@app.route('/places', methods=['GET'])
def read_places():
    from Persistence import data_manager as place_repository
    places = place_repository.all("Place")
    return jsonify([places[id].to_dict() for id in places]), 200

@app.route('/places/<id>', methods=['GET'])
def read_place(id):
    from Persistence import data_manager as place_repository
    place = place_repository.get(id, "Place")
    if place is None:
        return jsonify({"error": "Place not found"}), 404
    return jsonify(place.to_dict()), 200

@app.route('/places/<id>', methods=['PUT'])
def update_place(id):
    from Persistence import data_manager as place_repository
    place = place_repository.get(id, "Place")
    if place is None:
        return jsonify({"error": "Place not found"}), 404
    data = request.get_json()
    place_repository.update(place, **data)
    return jsonify(place.to_dict()), 200

@app.route('/places/<id>', methods=['DELETE'])
def delete_place(id):
    from Persistence import data_manager as place_repository
    place = place_repository.get(id, "Place")
    if place is None:
        return jsonify({"error": "Place not found"}), 404
    place_repository.delete(place, "Place")
    return jsonify({}), 204

@place_blueprint.route('/places', methods=['GET'])
def get_places():
    from Persistence import data_manager as place_repository
    all_places = place_repository.all("Place")  # Assurez-vous que cette méthode renvoie toutes les places
    return jsonify(all_places), 200

@place_blueprint.route('/places/<place_id>', methods=['GET'])
def get_place_details(place_id):
    from Persistence import data_manager as place_repository
    place = place_repository.find("Place", place_id)  # Implémentez cette recherche dans votre gestionnaire de données
    if place:
        return jsonify(place), 200
    else:
        return jsonify({"error": "Place not found"}), 404
