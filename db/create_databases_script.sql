DROP DATABASE IF EXISTS `ec_users`; 
CREATE DATABASE ec_users; 
USE ec_users; 

SET NAMES utf8;
SET character_set_client = utf8mb4 ;

CREATE TABLE logins(
	`user_id` INT AUTO_INCREMENT PRIMARY KEY, 
    `name` VARCHAR(20) NOT NULL UNIQUE, 
    `email` VARCHAR(50) NOT NULL UNIQUE, 
    `password` VARCHAR(50) NOT NULL,
    `admin` BOOL NOT NULL DEFAULT FALSE,
    `creation_date` DATE DEFAULT (CURDATE())
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO logins VALUES(1, 'ADMIN', 'admin@gmail.com', 'password', TRUE, DEFAULT); 

CREATE TABLE locations(
	`location_id` INT AUTO_INCREMENT PRIMARY KEY, 
    `user_id` INT,
    `country` VARCHAR (15), 
    `state` VARCHAR (15), 
    `city` VARCHAR (15), 
    `district` VARCHAR (15), 
    `street` VARCHAR (50), 
    FOREIGN KEY (`user_id`) REFERENCES logins(`user_id`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO locations values(1, 1, 'Brazil', 'Alagoas', 'Maceió', 'Ponta Verde', 'Sandoval Arroxelas'); 

DROP DATABASE IF EXISTS `ec_inventory`; 
CREATE DATABASE ec_inventory; 
USE ec_inventory; 

CREATE TABLE products(
	`product_id` INT AUTO_INCREMENT PRIMARY KEY, 
    `product_name` VARCHAR (50) NOT NULL UNIQUE, 
    `cost` DECIMAL (6, 2) NOT NULL,
    `quantity` INT NOT NULL, 
    `insertion_date` DATE DEFAULT (CURDATE())
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO products VALUES(1, 'Iphone 15 Pro Max', 7500.00, 70, CURDATE()); 