DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS suppliers;

CREATE TABLE suppliers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  description VARCHAR(255),
  quantity INT,
  buy_price INT,
  sell_price INT,
  category VARCHAR(255),
  supplier_id INT REFERENCES suppliers(id)
);