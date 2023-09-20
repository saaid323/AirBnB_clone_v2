-- script that prepares a MySQL server for the project:
CREATE  hbnb_test_db IF NOT EXISTS hbnb_test_db;
CREATE hbnb_test IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
