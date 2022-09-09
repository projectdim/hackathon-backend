CREATE SCHEMA dim_db;

CREATE TABLE dim_db.reviews
(
    id                 INTEGER PRIMARY KEY AUTOINCREMENT,
    ts                 TIMESTAMP   NOT NULL,
    latitude           NUMERIC(7)  NOT NULL,
    longitude          NUMERIC(7)  NOT NULL,
	city               VARCHAR(32) NOT NULL,
	street             VARCHAR(128) NOT NULL,
	zipcode            VARCHAR(6) NOT NULL,
    intact             INTEGER     NOT NULL,
    stable_electricity INTEGER     NOT NULL,
    accessible         INTEGER     NOT NULL,
    stable_water       INTEGER     NOT NULL,
    gas_station        INTEGER     NOT NULL,
    medical_facilities INTEGER     NOT NULL,
    comment            TEXT        NOT NULL,
    status             VARCHAR(32) NOT NULL
);

CREATE TABLE dim_db.events
(
    id                 INTEGER PRIMARY KEY AUTOINCREMENT,
    ts                 TIMESTAMP   NOT NULL,
    review_id          INTEGER,
	city               VARCHAR(32),
	street             VARCHAR(128),
	zipcode            VARCHAR(6),
    intact             INTEGER,
    stable_electricity INTEGER,
    accessible         INTEGER,
    stable_water       INTEGER,
    gas_station        INTEGER,
    medical_facilities INTEGER,
    comment            TEXT,
    status             VARCHAR(32),
    type               VARCHAR(10) NOT NULL
    FOREIGN KEY (review_id) REFERENCES reviews (id)
);

CREATE TABLE dim_db.images
(
    review_id INTEGER      NOT NULL,
    image_ref VARCHAR(500) NOT NULL,
    UNIQUE (image_ref)
);


