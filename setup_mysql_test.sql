-- Create a database in mysql
CREATE DATABASE IF NOT EXISTS hbnb_tets_db;
-- Create user in mysql
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Give privileges
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Give SELECT privileges 
GRANT SELECT ON 'performance_schema'.* TO 'hbnb_test'@'localhost';
-- Update privileges
FLUSH PRIVILEGES;
