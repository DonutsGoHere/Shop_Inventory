from db.run_sql import run_sql
from models.product import Product

import repositories.supplier_repository as supplier_repository

def save(product):
  sql = "INSERT INTO products (name, description, quantity, buy_price, sell_price, supplier_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING * "
  values = [product.name, product.description, product.quantity, product.buy_price, product.sell_price, product.supplier.id]
  results = run_sql(sql, values)
  id = results[0]['id']
  product.id = id
  return product

def select_all():
  products = []
  sql = "SELECT * FROM products"
  results = run_sql(sql)

  for res in results:
    supplier = supplier_repository.select(res['supplier_id'])
    product = Product(res['name'], res['description'], supplier, res['quantity'], res['buy_price'], res['sell_price'])
    products.append(product)
  return products

def select(id):
  product = None
  sql = "SELECT * FROM products WHERE id = %s"
  values = [id]
  result = run_sql(sql, values)[0]

  if result is not None:
    supplier = supplier_repository.select(result['supplier_id'])
    product = Product(result['name'], result['description'], supplier, result['quantity'], result['buy_price'], result['sell_price'] )
  return product

def update(product):
  sql = "UPDATE products SET (name, description, quantity, buy_price, sell_price, supplier_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
  values = [product.name, product.description, product.quantity, product.buy_price, product.sell_price, product.supplier.id]
  run_sql(sql, values)

def delete_all():
  sql = "DELETE  FROM products"
  run_sql(sql)

def delete(id):
  sql = "DELETE  FROM products WHERE id = %s"
  values = [id]
  run_sql(sql, values)
