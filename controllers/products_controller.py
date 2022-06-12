from flask import Flask, render_template
from flask import Blueprint
from models.product import Product
import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository

product_repository = Blueprint("products", __name__)