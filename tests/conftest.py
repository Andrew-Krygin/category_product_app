import copy

import pytest

from models.category import Category
from models.product import Product
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
