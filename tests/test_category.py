import pytest

from models.category import Category
from tests.tests_data.data_for_models import list_products


@pytest.fixture
def test_category() -> Category:
    Category.cnt_categories = 0
    Category.cnt_products = 0
    return Category("Смартфоны", "Смартфоны, лучшее что придумало человечество.", list_products)


class TestCategory:
    def test_init_category(self, test_category: Category) -> None:
        assert isinstance(test_category, Category)
        assert test_category.name == "Смартфоны"
        assert test_category.description == "Смартфоны, лучшее что придумало человечество."
        assert test_category.cnt_categories == 1
        assert test_category.cnt_products == len(list_products)
