import pdb
from flask import render_template, Blueprint, request, redirect
from repositories import product_repository, supplier_repository
from models.product import Product
from models.supplier import Supplier

product_blueprint = Blueprint("products", __name__)

@product_blueprint.route('/products')
def products():
    all_products_list = product_repository.select_all()
    return render_template('products/index.html', all_products=all_products_list)

@product_blueprint.route('/products/new')
def new_product():
    suppliers = supplier_repository.select_all()
    return render_template('products/new.html', all_suppliers=suppliers)

@product_blueprint.route('/products', methods=['POST'])
def save_product():
    name = request.form['name']
    supplier_id = request.form['supplier_id']
    supplier = supplier_repository.select(supplier_id)
    description = request.form['description']
    stock_quantity = request.form['stock_quantity']
    buying_price = request.form['buying_price']
    selling_price = request.form['selling_price']
    product = Product(name, supplier, description, stock_quantity, buying_price, selling_price)
    product_repository.save(product)
    return redirect('/products')

@product_blueprint.route('/products/<id>', methods=['POST'])
def update_product(id):
    name = request.form['name']
    supplier = supplier_repository.select(request.form['supplier_id'])
    description = request.form['description']
    stock_quantity = request.form['stock_quantity']
    buying_price = request.form['buying_price']
    selling_price = request.form['selling_price']
    product = Product(name, supplier, description, stock_quantity, buying_price, selling_price, id)
    product_repository.update(product)
    return redirect('/products')


@product_blueprint.route('/products/<id>')
def get_product(id):
    product = product_repository.select(id)
    return render_template('products/show.html', product=product)

@product_blueprint.route('/products/<id>/edit')
def edit_products(id):
    product = product_repository.select(id)
    suppliers = supplier_repository.select_all()
    return render_template('products/edit.html', all_suppliers=suppliers, product=product)

@product_blueprint.route('/products/<id>/delete', methods=['POST'])
def remove_product(id):
    product_repository.delete(id)
    return redirect('/products')