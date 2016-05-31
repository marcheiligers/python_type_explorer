class TypePrinter:
  def __init__(self, typ):
    self.typ = typ

  def __str__(self):
    return str(self.typ)

StringTypePrinter = TypePrinter