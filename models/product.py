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

  def calculate_mark_up(self):
    mark_up = (self.sell_price) - (self.buy_price)
    return mark_up

  def stock_indicator(self):
    if self.quantity >= 10:
      return ""
    if self.quantity < 10:
      return "low stock"
    elif self.quantity == 0:
      return "out of stock"