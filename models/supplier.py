class Supplier:
  def __init__(self, name, id = None):
    self.name = name
    self.id = id

  def sup_name(self):
    return f"{self.name}"