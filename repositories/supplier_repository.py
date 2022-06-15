from db.run_sql import run_sql
from models.supplier import Supplier
from models.product import Product

def save(supplier):
  sql = "INSERT INTO suppliers (name) VALUES (%s) RETURNING *"
  values = [supplier.name]
  results = run_sql(sql, values)
  id = results[0]['id']
  supplier.id = id
  return supplier

def select_all():
  suppliers = []

  sql = "SELECT * FROM suppliers"
  results = run_sql(sql)

  for res in results:
    supplier = Supplier(res['name'], res['id'])
    suppliers.append(supplier)
  return suppliers

def select(id):
  supplier = None
  sql = "SELECT * FROM suppliers WHERE id = %s"
  values = [id]
  result = run_sql(sql, values)[0]

  if result is not None:
    supplier = Supplier(result['name'], result['id'])
  return supplier

def update(supplier):
  sql = "UPDATE suppliers SET name = %s WHERE id = %s"
  values = [supplier.name, supplier.id]
  run_sql(sql, values)

def delete_all():
  sql = "DELETE  FROM suppliers"
  run_sql(sql)

def delete(id):
  sql = "DELETE  FROM suppliers WHERE id = %s"
  values = [id]
  run_sql(sql, values)