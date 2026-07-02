CREATE DATABASE IF NOT EXISTS mydatabase;

USE mydatabase;

CREATE TABLE IF NOT EXISTS images (
    id INT AUTO_INCREMENT PRIMARY KEY,
    image_name VARCHAR(255) NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO images (image_name, file_path)
VALUES ('Product 1', 'catalog/product1.svg');

INSERT INTO images (image_name, file_path)
VALUES ('Product 2', 'catalog/product2.svg');

UPDATE images
SET file_path = 'catalog/featured/product1.svg'
WHERE image_name = 'Product 1';
