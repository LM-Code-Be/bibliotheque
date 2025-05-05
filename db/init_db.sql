-- init_db.sql – création rapide de la BD
CREATE DATABASE IF NOT EXISTS bibliotheque
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE bibliotheque;

DROP TABLE IF EXISTS books;
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title     VARCHAR(255) NOT NULL,
    author    VARCHAR(255),
    summary   TEXT,
    read_date DATE,
    note      TINYINT CHECK (note BETWEEN 0 AND 10),
    status    ENUM('à lire','en cours','lu') DEFAULT 'à lire'
);
