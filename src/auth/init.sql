  CREATE USER 'auth_user'@'localhost' IDENTIFIED BY 'auth123';

  CREATE DATABASE auth;

  GRANT ALL PRIVILEGES ON auth.* TO 'auth_user'@'localhost';

  USE auth;

  CREATE TABLE user (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(225) UNIQUE NOT NULL,
    password VARCHAR(225) NOT NULL
  );

  INSERT INTO user(email, password) VALUES ('amin@email.com', 'admin')