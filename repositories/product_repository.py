import pdb
from db.run_sql import run_sql

from models.product import Product
from models.supplier import Supplier
import repositories.supplier_repository as supplier_repository

def save(product):
    sql = "INSERT INTO products (name, supplier_id, description, stock_quantity, buying_price, selling_price) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [product.name, product.supplier.id, product.description, product.stock_quantity, product.buying_price, product.selling_price]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product


def select_all():
    products = []

    sql = "SELECT * FROM products"
    results = run_sql(sql)

    for row in results:
        supplier = supplier_repository.select(row['supplier_id'])
        product = Product(row['name'], supplier, row['description'], row['stock_quantity'], row['buying_price'], row['selling_price'], row['id'])
        products.append(product)
    return products


def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        supplier = supplier_repository.select(result['supplier_id'])
        product = Product(result['name'], supplier, result['description'], result['stock_quantity'], result['buying_price'], result['selling_price'], result['id'])
    return product


def sort_alphabetically():
    products = select_all()
    products.sort(key=lambda x: x.name)
    return products


def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(product):
    sql = "UPDATE products SET (name, supplier_id, description, stock_quantity, buying_price, selling_price) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [product.name, product.supplier.id, product.description, product.stock_quantity, product.buying_price, product.selling_price, product.id]
    print(values)
    run_sql(sql, values)