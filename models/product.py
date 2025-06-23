class Product:
    """Класс для представления продуктов."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __eq__(self, other):
        return (isinstance(other, Product) and
                self.name == other.name and
                self.description == other.description and
                self.price == other.price and
                self.quantity == other.quantity)