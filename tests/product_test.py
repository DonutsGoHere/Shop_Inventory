import unittest
from models.product import Product
from models.supplier import Supplier

class TestProductMethods(unittest.TestCase):

  def setUp(self):
    supplier_1 = Supplier("Madbury\'s Chocolate")

    self.product_1 = Product("Milk Chocolate Bar", "40g single bar", supplier_1, 10, 1, 2, "sweets")

    self.product_2 = Product("Dark Chocolate Bar", "40g single bar", supplier_1, 5, 1, 2, "sweets")

    self.product_3 = Product("White Chocolate Bar", "40g single bar", supplier_1, 0, 1, 2, "sweets")


  def test_indicates_stock(self):
    self.assertEqual("", self.product_1.stock_indicator())

  def test_indicates_low_stock(self):
    self.assertEqual("low stock", self.product_2.stock_indicator())

  def test_indicates_out_of_stock(self):
    self.assertEqual("** out of stock! **", self.product_3.stock_indicator())

  def test_shows_mark_up(self):
    self.assertEqual(1, self.product_1.calculate_mark_up())