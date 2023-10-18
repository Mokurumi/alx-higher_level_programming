-- creates the database hbtn_0d_usa in MySQL server.
-- creates table states with cols id and name
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `states` (
    `id` INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` VARCHAR(256) NOT NULL
);
