--This script setup a database
CREATE DATABASE IF NOT EXIST hbnb_dev_db;
CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'r1';
sudo service mysql restart
