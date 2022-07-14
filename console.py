import pdb
from models.product import Product
from models.supplier import Supplier

import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository


product_repository.delete_all()
supplier_repository.delete_all()


supplier_1 = Supplier("Madbury\'s Chocolate")
supplier_repository.save(supplier_1)

supplier_2 = Supplier("Porky Pete\'s Pork stuff")
supplier_repository.save(supplier_2)

supplier_3 = Supplier("Danger Dave\'s Distribution")
supplier_repository.save(supplier_3)



product_1 = Product("Milk Chocolate Bar", "40g single bar", supplier_1, 10, 1, 2, "sweets")
product_repository.save(product_1)

product_2 = Product("Dark Chocolate Bar", "40g single bar", supplier_1, 5, 1, 2, "sweets")
product_repository.save(product_2)

product_3 = Product("White Chocolate Bar", "40g single bar", supplier_1, 5, 1, 2, "sweets")
product_repository.save(product_3)

product_4 = Product("Pork Scratching\'s", "100g grab bag", supplier_2, 10, 2, 4, "savory snacks")
product_repository.save(product_4)

product_5 = Product("Prime Pork Scratching\'s", "40g snack bag", supplier_2, 20, 1, 3, "savory snacks")
product_repository.save(product_5)

product_6 = Product("Pork Crunch", "40g snack bag", supplier_2, 10, 1, 2, "savory snacks")
product_repository.save(product_6)

product_7 = Product("Blue Cow Energy Drink", "125ml single can", supplier_3, 15, 1, 3, "drinks")
product_repository.save(product_7)

product_8 = Product("Blue Cow: An Udder", "4 x 125ml Blue Cow Energy Drink multipack", supplier_3, 10, 2, 6, "drinks")
product_repository.save(product_8)

product_9 = Product("Flying Blue Cow Energy Drink: ENERGY FREE, ZERO PURPOSE ALTERNATIVE!", "125ml single can", supplier_3, 2, 1, 3, "drinks")
product_repository.save(product_9)

product_10 = Product("CHALK: The original Chalk beverage", "2l large bottle", supplier_3, 0, 2, 4, "drinks")
product_repository.save(product_10)

pdb.set_trace()