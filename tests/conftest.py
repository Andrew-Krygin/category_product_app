import copy

import pytest

from models.category import Category
from models.product import LawnGrass, Product, Smartphone
from tests.tests_data.data_for_models import list_products


@pytest.fixture
def sample_category() -> Category:
    Category.cnt_categories = 0
    Category.cnt_products = 0

    fresh_products = copy.deepcopy(list_products)

    return Category("Смартфоны", "Смартфоны, лучшее что придумало человечество.", fresh_products)


@pytest.fixture
def sample_products() -> Product:
    return Product("Iphone 15", "512GB, Gray space", 31000.0, 14)


@pytest.fixture
def sample_smartphone() -> Smartphone:
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def sample_lawn_grass() -> LawnGrass:
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
