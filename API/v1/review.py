from flask import request, jsonify
from API.v1.app import app
from Persistence.datamanager import data_manager
from Model.review import Review

@app.route('/places/<place_id>/reviews', methods=['POST'])
def create_review():
    data = request.get_json()
    review = Review(**data)
    review_repository.save(review)
    return jsonify(review.to_dict()), 201

#Il te faut un POST /places/{place_id}/reviews pour créer une review
#Il te faut un GET /places/{place_id}/reviews pour récupérer les reviews d'un place
#Il te faut un DELETE /reviews/{review_id} pour supprimer une review
#Il te faut un PUT /reviews/{review_id} pour modifier une review

#Il te faut un GET /users/{user_id}/reviews pour récupérer les reviews d'un user
@app.route('/users/<user_id>/reviews', methods=['GET'])
def get_user_reviews(user_id):
    user = data_manager.get(user_id, "User")
    if user is None:
        return jsonify({"error": "User not found"}), 404
    reviews = user.reviews
    return jsonify([review.to_dict() for review in reviews]), 200

@app.route('/users/<user_id>/reviews', methods=['GET'])
def read_reviews():
    reviews = data_manager.all("Review")
    return jsonify([reviews[id].to_dict() for id in reviews]), 200

@app.route('/places/<place_id>/reviews', methods=['GET'])
def read_review(id):
    reviews = data_manager.get(id, "Review")
    if reviews is None:
        return jsonify({"error": "Review not found"}), 404
    return jsonify(reviews.to_dict()), 200

@app.route('/reviews/<review_id>', methods=['PUT'])
def update_review(id):
    review = data_manager.get(id, "Review")
    if review is None:
        return jsonify({"error": "Review not found"}), 404
    data = request.get_json()
    data_manager.update(review, **data)
    return jsonify(review.to_dict()), 200

@app.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(id):
    review = data_manager.get(id, "Review")
    if review is None:
        return jsonify({"error": "Review not found"}), 404
    data_manager.delete(review, "Review")
    return jsonify({}), 204
