from models.abstracts import BaseEntity
from models.category import Category
from models.product import Product
from tests.tests_data.data_for_models import category_for_order


class Order(BaseEntity):
    """Класс представляет товар, который был куплен и количество купленного товара."""

    def __init__(self, name: str, description: str, category: Category, product_name: str, quantity: int) -> None:
        super().__init__(name, description)
        self.category = category
        self.product_name = product_name
        self.quantity = quantity
        self.product = self.find_product()
        self.cost = self.get_cost()

    def __str__(self) -> str:
        if self.product:
            return (
                f"Заказ: {self.name}\n"
                f"Описание: {self.description}\n"
                f"Товар: {self.product.name}\n"
                f"Количество куплено: {self.quantity}\n"
                f"Стоимость: {self.cost} руб.\n"
                f"Остаток на складе: {self.product.quantity} шт."
            )
        else:
            return f"Товар '{self.product_name}' не найден."

    def find_product(self) -> Product | None:
        for prod in self.category.products:
            if prod.name == self.product_name:
                res: Product = prod
                return res
        return None

    def get_cost(self) -> float:
        if self.product is None:
            raise ValueError(f"Товар '{self.product_name}' не найден в категории.")

        if self.product.quantity < self.quantity:
            raise ValueError(
                f"Недостаточно товара '{self.product_name}' на складе.\n"
                f"Доступно: {self.product.quantity}, запрошено: {self.quantity}."
            )

        self.product.quantity -= self.quantity
        return self.product.price * self.quantity
