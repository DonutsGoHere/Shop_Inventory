from flask import Flask, render_template
from flask import Blueprint
from models.supplier import Supplier
import repositories.supplier_repository as supplier_repository
import repositories.product_repository as product_repository

suppliers_blueprint = Blueprint("suppliers", __name__)


# INDEX
# GET '/suppliers'
@suppliers_blueprint.route("/suppliers")
def suppliers():
  suppliers = supplier_repository.select_all()
  return render_template("suppliers/index.html", all_suppliers = suppliers)

# NEW
# GET '/suppliers/new'

# CREATE
# POST '/suppliers'

# SHOW
# GET '/suppliers/<id>'

# EDIT
# GET '/suppliers/<id>/edit'

# UPDATE
# PUT '/suppliers/<id>'

# DELETE
# DELETE '/suppliers/<id>'