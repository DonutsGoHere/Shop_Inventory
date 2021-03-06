from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.supplier import Supplier
from models.product import Product
import repositories.supplier_repository as supplier_repository
import repositories.product_repository as product_repository

suppliers_blueprint = Blueprint("suppliers", __name__)

@suppliers_blueprint.route("/suppliers")
def suppliers():
  suppliers = supplier_repository.select_all()
  products = product_repository.select_all()
  return render_template("suppliers/index.html", all_suppliers = suppliers, all_products = products)

@suppliers_blueprint.route("/suppliers/new", methods=['GET'])
def new_supplier():
  suppliers = supplier_repository.select_all()
  return render_template("suppliers/new.html", all_suppliers = suppliers)


@suppliers_blueprint.route("/suppliers", methods=['POST'])
def create_supplier():
  name = request.form['name']
  supplier = Supplier(name)
  supplier_repository.save(supplier)
  return redirect('/suppliers')

@suppliers_blueprint.route("/suppliers/<id>", methods=['GET'])
def show_supplier(id):
  supplier = supplier_repository.select(id)
  return render_template('suppliers/show.html', supplier = supplier)


@suppliers_blueprint.route("/suppliers/<id>/edit", methods=['GET'])
def edit_supplier(id):
  supplier = supplier_repository.select(id)
  products = product_repository.select_all()
  return render_template('suppliers/edit.html', supplier = supplier, all_products = products)


@suppliers_blueprint.route("/suppliers/<id>", methods=['POST'])
def update_supplier(id):
  name = request.form['name']
  supplier = Supplier(name, id)
  supplier_repository.update(supplier)
  return redirect('/suppliers')


@suppliers_blueprint.route("/suppliers/<id>/delete", methods=['POST'])
def delete_book(id):
  supplier_repository.delete(id)
  return redirect('/suppliers')