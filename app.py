from flask import Flask, render_template

import repositories.product_repository as product_repository
from controllers.products_controller import products_blueprint
from controllers.suppliers_controller import suppliers_blueprint

app = Flask(__name__)

app.register_blueprint(products_blueprint)
app.register_blueprint(suppliers_blueprint)

@app.route('/')
def home():
    products = product_repository.select_all()
    return render_template('index.html', all_products = products)

if __name__ == '__main__':
    app.run(debug=True)