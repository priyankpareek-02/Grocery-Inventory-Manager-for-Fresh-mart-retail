
-- Create database
CREATE DATABASE IF NOT EXISTS grocery_inventory;
USE grocery_inventory;

-- Create products table
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    price_per_unit DECIMAL(10,2) NOT NULL
);

-- Insert sample products
INSERT INTO products (name, quantity, price_per_unit) VALUES
('Tomatoes', 10, 20.00),
('Potatoes', 3, 15.50),
('Milk', 5, 42.00),
('Rice', 2, 50.00);
