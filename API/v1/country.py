from flask import request, jsonify
from API.v1.app import app
from Persistence.datamanager import data_manager

@app.route('/countries', methods=['GET'])
def read_countries():
    countries = data_manager.read_database("countries")
    return jsonify([country for country in countries]), 200

@app.route('/countries/<country_code>', methods=['GET'])
def read_country(country_code):
    countries = data_manager.read_database("countries")
    for country in countries:
        if (country["code"] == country_code):
            return jsonify(country), 200
    return jsonify({"error": "Country not found"}), 404

@app.route('/countries/<country_code>/cities', methods=['GET'])
def read_country_cities(country_code):
    all_cities = data_manager.all("City")
    country_cities = []

    for city_id in all_cities:
        current_city = all_cities[city_id]
        if (current_city.country_code == country_code):
            country_cities.append(current_city.to_dict())
    return jsonify(country_cities), 200
    # if country is None:
    #     return jsonify({"error": "Country not found"}), 404
    # cities = country.cities
    # return jsonify([city.to_dict() for city in cities]), 200
