-- This script setup a database
-- Create db
CREATE DATABASE IF NOT EXIST hbnb_dev_db;
-- create user and passwd
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Privileges
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Privileges select
GRANT SELECT ON performance_schema.* TO 'r1';
