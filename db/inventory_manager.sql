DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS suppliers;

CREATE TABLE suppliers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  contact_details VARCHAR(255)
);

CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  supplier_id INT NOT NULL REFERENCES suppliers(id),
  description VARCHAR(255),
  stock_quantity INT NOT NULL,
  buying_price DECIMAL(5, 2) NOT NULL,
  selling_price DECIMAL(5, 2) NOT NULL
  );