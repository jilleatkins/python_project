from db.run_sql import run_sql

from models.supplier import Supplier
from models.product import Product

def save(supplier):
    sql = "INSERT INTO suppliers (name, contact_details) VALUES (%s, %s) RETURNING *"
    values = [supplier.name, supplier.contact_details]
    results = run_sql(sql, values)
    id = results[0]['id']
    supplier.id = id
    return supplier


def select_all():
    suppliers = []

    sql = "SELECT * FROM suppliers"
    results = run_sql(sql)

    for row in results:
        supplier = Supplier(row['name'], row['contact_details'], row['id'] )
        suppliers.append(supplier)
    return suppliers


def select(id):
    supplier = None
    sql = "SELECT * FROM suppliers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        supplier = Supplier(result['name'], result['contact_details'], result['id'] )
    return supplier


def delete_all():
    sql = "DELETE FROM suppliers"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM suppliers WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(supplier):
    sql = "UPDATE suppliers SET (name, contact_details) = (%s, %s) WHERE id = %s"
    values = [supplier.name, supplier.contact_details, supplier.id]
    run_sql(sql, values)

def products(supplier):
    products = []

    sql = "SELECT * FROM products WHERE supplier_id = %s"
    values = [supplier.id]
    results = run_sql(sql, values)

    for row in results:
        product = Product(row['name'], supplier, row['description'], row['stock_quantity'], row['buying_price'], row['selling_price'], row['id'])
        products.append(product)
    return products