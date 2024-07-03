-- ================================================================
-- this file contents all scripts to create the database in SQLite
-- ================================================================ 

CREATE DATABASE IF NOT EXISTS hbnbdatabase;

USE hbnbdatabase;

CREATE TABLE IF NOT EXISTS users (
    id VARCHAR(255) PRIMARY KEY NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    first_name VARCHAR(255)  NOT NULL DEFAULT '',
    last_name VARCHAR(255)  NOT NULL DEFAULT '',
    is_admin BOOLEAN DEFAULT FALSE,
    `role` VARCHAR(255) DEFAULT 'user',    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS cities (
    id VARCHAR(255) PRIMARY KEY NOT NULL,
    name VARCHAR(255) NOT NULL,
    population INT NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS countries (
    id VARCHAR(255) PRIMARY KEY NOT NULL,
    name VARCHAR(255) NOT NULL,
    population INT NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS amenities (
    id VARCHAR(255) PRIMARY KEY NOT NULL,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(1024),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS places (
    id VARCHAR(255) PRIMARY KEY NOT NULL,
    user_id VARCHAR(255) NOT NULL,
    city_id VARCHAR(255) NOT NULL,
    review_id VARCHAR(255) NOT NULL,
    amenity_id VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS reviews (
    id VARCHAR(255) PRIMARY KEY NOT NULL,
    text VARCHAR(255) NOT NULL,
    user_id VARCHAR(255) NOT NULL,
    place_id VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Ajout des contraintes de clé étrangère après la création de toutes les tables
ALTER TABLE places
ADD CONSTRAINT fk_places_user_id FOREIGN KEY (user_id) REFERENCES users(id),
ADD CONSTRAINT fk_places_city_id FOREIGN KEY (city_id) REFERENCES cities(id),
ADD CONSTRAINT fk_places_amenity_id FOREIGN KEY (amenity_id) REFERENCES amenities(id);

ALTER TABLE reviews
ADD CONSTRAINT fk_reviews_user_id FOREIGN KEY (user_id) REFERENCES users(id),
ADD CONSTRAINT fk_reviews_place_id FOREIGN KEY (place_id) REFERENCES places(id);
