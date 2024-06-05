-- create_db.sql

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS chameleon_db;

-- Use the database
USE chameleon_db;

-- Create a table if it doesn't exist
CREATE TABLE IF NOT EXISTS attributes_keys (
    attribute_id INT PRIMARY KEY AUTO_INCREMENT,
    attribute_name VARCHAR(255),
    Chicken FLOAT DEFAULT 0,
    Pizza FLOAT DEFAULT 0,
    Burger FLOAT DEFAULT 0,
    Salad FLOAT DEFAULT 0,
    Pasta FLOAT DEFAULT 0,
    Sushi FLOAT DEFAULT 0,
    Steak FLOAT DEFAULT 0,
    Tacos FLOAT DEFAULT 0,
    Soup FLOAT DEFAULT 0,
    Sandwich FLOAT DEFAULT 0,
    Fries FLOAT DEFAULT 0,
    Hotdog FLOAT DEFAULT 0,
    Curry FLOAT DEFAULT 0,
    Rice FLOAT DEFAULT 0,
    Fish FLOAT DEFAULT 0,
    Cake FLOAT DEFAULT 0
);

CREATE TABLE IF NOT EXISTS attributes_keys_probability (
    attribute_id INT PRIMARY KEY,
    attribute_name VARCHAR(255),
    Chicken FLOAT DEFAULT 0,
    Pizza FLOAT DEFAULT 0,
    Burger FLOAT DEFAULT 0,
    Salad FLOAT DEFAULT 0,
    Pasta FLOAT DEFAULT 0,
    Sushi FLOAT DEFAULT 0,
    Steak FLOAT DEFAULT 0,
    Tacos FLOAT DEFAULT 0,
    Soup FLOAT DEFAULT 0,
    Sandwich FLOAT DEFAULT 0,
    Fries FLOAT DEFAULT 0,
    Hotdog FLOAT DEFAULT 0,
    Curry FLOAT DEFAULT 0,
    Rice FLOAT DEFAULT 0,
    Fish FLOAT DEFAULT 0,
    Cake FLOAT DEFAULT 0
);

CREATE TABLE IF NOT EXISTS naive_bayes (
    keyword VARCHAR(255) PRIMARY KEY,
    probability FLOAT DEFAULT 0
);

CREATE TABLE IF NOT EXISTS word2vec (
    keyword VARCHAR(255) PRIMARY KEY,
    probability FLOAT DEFAULT 0
);

CREATE TABLE IF NOT EXISTS attributes_spreading (
    attribute_id INT PRIMARY KEY,
    attribute_name VARCHAR(255),
    key_word_covering INT
);

