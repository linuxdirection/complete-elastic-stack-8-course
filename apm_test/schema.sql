-- Schema file: schema.sql

-- Create the database
CREATE DATABASE IF NOT EXISTS testdb;
USE testdb;

-- Create a primary test table
CREATE TABLE IF NOT EXISTS test_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    created_at DATETIME
);

-- Create another table for JOIN queries
CREATE TABLE IF NOT EXISTS another_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    test_table_id INT,
    description VARCHAR(100),
    FOREIGN KEY (test_table_id) REFERENCES test_table(id)
);

-- Insert sample data into test_table
INSERT INTO test_table (name, created_at) VALUES ('Alice', '2023-01-01 10:00:00');       
INSERT INTO test_table (name, created_at) VALUES ('Bob', '2023-01-02 11:00:00');
INSERT INTO test_table (name, created_at) VALUES ('Charlie', '2023-01-03 12:00:00');     

-- Insert sample data into another_table
INSERT INTO another_table (test_table_id, description) VALUES (1, 'Description for Alice');
INSERT INTO another_table (test_table_id, description) VALUES (2, 'Description for Bob');
INSERT INTO another_table (test_table_id, description) VALUES (3, 'Description for Charlie');