CREATE SCHEMA dim_db;

CREATE TABLE dim_db.reviews (
	id SERIAL PRIMARY KEY,
	ts TIMESTAMP NOT NULL,
	latitude NUMERIC(7) NOT NULL,
	longitude NUMERIC(7) NOT NULL,
	city VARCHAR(32) NOT NULL,
	street VARCHAR(128) NOT NULL,
	zipcode VARCHAR(6) NOT NULL,
	building_status VARCHAR(32) NOT NULL,
	building_safety_level INTEGER NOT NULL,
	building_description TEXT NOT NULL,
	electricity_status VARCHAR(32) NOT NULL,
	electricity_safety_level INTEGER NOT NULL,
	electricity_description TEXT NOT NULL,
	water_status VARCHAR(32) NOT NULL,
	water_safety_level INTEGER NOT NULL,
	water_description TEXT NOT NULL,
	road_status VARCHAR(32) NOT NULL,
	road_safety_level INTEGER NOT NULL,
	road_description TEXT NOT NULL,
	fuel_status VARCHAR(32) NOT NULL,
	fuel_safety_level INTEGER NOT NULL,
	fuel_description TEXT NOT NULL,
	medical_facilities_status VARCHAR(32) NOT NULL,
	medical_facilities_safety_level INTEGER NOT NULL,
	medical_facilities_description TEXT NOT NULL,
	comment TEXT NOT NULL,
	status VARCHAR(32) NOT NULL
);

CREATE TABLE dim_db.events (
	id SERIAL PRIMARY KEY,
	ts TIMESTAMP NOT NULL,
	review_id INTEGER,
	city VARCHAR(32),
	street VARCHAR(128),
	zipcode VARCHAR(6),
	building_status VARCHAR(32),
	building_safety_level INTEGER,
	building_description TEXT,
	electricity_status VARCHAR(32),
	electricity_safety_level INTEGER,
	electricity_description TEXT,
	water_status VARCHAR(32),
	water_safety_level INTEGER,
	water_description TEXT,
	road_status VARCHAR(32),
	road_safety_level INTEGER,
	road_description TEXT,
	fuel_status VARCHAR(32),
	fuel_safety_level INTEGER,
	fuel_description TEXT,
	medical_facilities_status VARCHAR(32),
	medical_facilities_safety_level INTEGER,
	medical_facilities_description TEXT,
	comment TEXT,
	status VARCHAR(32),
	type VARCHAR(10),
	FOREIGN KEY (review_id) REFERENCES reviews (id)
);

CREATE TABLE dim_db.images (
	review_id INTEGER NOT NULL,
	image_ref VARCHAR(500) NOT NULL,
	UNIQUE(image_ref),
	FOREIGN KEY (review_id) REFERENCES reviews (id)
);


