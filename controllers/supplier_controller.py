import pdb
from flask import render_template, Blueprint, redirect, request
from repositories import product_repository, supplier_repository
from models.supplier import Supplier
from models.product import Product

product_blueprint = Blueprint("products", __name__)
supplier_blueprint = Blueprint("suppliers", __name__)

@supplier_blueprint.route('/suppliers')
def suppliers():
    all_suppliers_list = supplier_repository.select_all()
    return render_template('suppliers/index.html', all_suppliers=all_suppliers_list)

@supplier_blueprint.route('/suppliers/<supplier_id>', methods=['POST'])
def update_supplier(supplier_id):
    name = request.form['name']
    contact_details = request.form['contact_details']
    supplier = Supplier(name, contact_details, supplier_id)
    supplier_repository.update(supplier)
    return redirect('/suppliers')

@supplier_blueprint.route('/suppliers/new')
def new_supplier():
    suppliers = supplier_repository.select_all()
    return render_template('suppliers/new.html', all_suppliers=suppliers)

@product_blueprint.route('/suppliers', methods=['POST'])
def supplier():
    name = request.form['name']
    contact_details = request.form['contact_details']
    supplier = Supplier(name, contact_details)
    product_repository.save(supplier)
    return redirect('/suppliers')



@supplier_blueprint.route('/suppliers/<supplier_id>')
def get_supplier(supplier_id):
    supplier = supplier_repository.select(supplier_id)
    return render_template('suppliers/show.html', supplier=supplier)

@supplier_blueprint.route('/suppliers/<supplier_id>/edit')
def edit_supplier(supplier_id):
    supplier = supplier_repository.select(supplier_id)
    products = product_repository.select_all()
    return render_template('suppliers/edit.html', supplier=supplier, products=products)

@supplier_blueprint.route('/suppliers/<supplier_id>/delete', methods=['POST'])
def remove_supplier(supplier_id):
    # pdb.set_trace()
    supplier_repository.delete(supplier_id)
    return redirect('/suppliers')