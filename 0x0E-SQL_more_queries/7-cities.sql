-- a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.

-- Create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- use the database created
USE hbtn_0d_usa;

-- create table cities
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
);
