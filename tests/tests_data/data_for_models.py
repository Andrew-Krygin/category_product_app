from contextlib import nullcontext as does_not_raise

import pytest

from models.product import Product

# Список продуктов для класса Category
list_products = [
    Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
    Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
    Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
]

# Корректный продукт для тестирования класса Product.
valid_case_new_product = (
    {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    },
    Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
    does_not_raise(),
)

# Некорректный продукт для тестирования класса Product.
invalid_case_new_product = (
    {"name": "Samsung Galaxy C23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0},
    None,
    pytest.raises(ValueError, match="A key required to create an object of " "class Product is missing."),
)
