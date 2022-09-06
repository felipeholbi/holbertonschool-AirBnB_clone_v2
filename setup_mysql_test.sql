-- This script prepare the mysql to setup
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create a database in mysql if not exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Create user in mysql if not exist
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Give all privileges to the current user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- Give SELECT privileges on the select DB
