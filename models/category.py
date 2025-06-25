class Category:
    """Класс для представления категорий."""

    cnt_categories = 0
    cnt_products = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products

        Category.cnt_categories += 1
        Category.cnt_products += len(self.products)

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, Category)
            and self.name == other.name
            and self.description == other.description
            and self.products == other.products
        )
