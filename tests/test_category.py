import copy

import pytest

from models.category import Category
from models.product import Product
from tests.tests_data.data_for_models import list_products


@pytest.fixture
def test_category() -> Category:
    Category.cnt_categories = 0
    Category.cnt_products = 0

    fresh_products = copy.deepcopy(list_products)

    return Category("Смартфоны", "Смартфоны, лучшее что придумало человечество.", fresh_products)


class TestCategory:
    def test_init_category(self, test_category: Category) -> None:
        assert isinstance(test_category, Category)
        assert test_category.name == "Смартфоны"
        assert test_category.description == "Смартфоны, лучшее что придумало человечество."
        assert test_category.cnt_categories == 1
        assert test_category.cnt_products == len(list_products)

    def test_products(self, test_category: Category) -> None:
        assert test_category.products == list_products
        assert isinstance(test_category.products, list)

    def test_add_products(self, test_category: Category) -> None:
        test_category.add_product(Product("Banana", "Ripe banana", 2.0, 20))
        assert test_category.cnt_products == 4

    @pytest.mark.parametrize(
        "input_data, ex_res, ex_cnt, ex_price",
        [
            (Product("Banana", "Ripe banana", 2.0, 20), False, 20, 2.0),
            (Product("Iphone 15", "512GB, Gray space", 210000.0, 8), True, 16, 210000.0),
            (Product("Xiaomi Redmi Note 11", "1024GB, Синий", 37000.0, 14), True, 28, 37000.0),
        ],
    )
    def test_product_exists(
        self, test_category: Category, input_data: Product, ex_res: bool, ex_cnt: int, ex_price: float
    ) -> None:
        assert test_category.product_exists(input_data) == ex_res

        found_product = next((prod for prod in test_category.products if prod.name == input_data.name), None)
        if ex_res:
            assert found_product is not None
            assert found_product.quantity == ex_cnt
            assert found_product.price == ex_price
        else:
            assert found_product is None
