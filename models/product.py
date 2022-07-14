class Product():
  def __init__(self, name, description, supplier, quantity, buy_price, sell_price, category, id = None):
    self.name = name
    self.description = description
    self.supplier = supplier
    self.quantity = quantity
    self.buy_price = buy_price
    self.sell_price = sell_price
    self.category = category
    self.id = id

# FUNCTION to ITERATE through product quantity
#  IF number is EQUAL to 0 THEN
#    DISPLAY "** out of stock! **"
#  IF number is LESS than 0 THEN
#    DISPLAY "low stock"
#  ELSE IF number is EQUAL to OR GREATER than 10 THEN
#    DISPLAY "empty string"

  def stock_indicator(self):
    if self.quantity == 0:
      return "** out of stock! **"
    if self.quantity < 10:
      return "low stock"
    elif self.quantity >= 10:
      return ""




  def calculate_mark_up(self):
    mark_up = (self.sell_price) - (self.buy_price)
    return mark_up