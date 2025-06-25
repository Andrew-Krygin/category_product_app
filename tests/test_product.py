import pytest

from models.product import Product


@pytest.fixture
def test_products() -> Product:
    return Product("Iphone 15", "512GB, Gray space", 31000.0, 14)


class TestProduct:
    def test_init_product(self, test_products: Product) -> None:
        assert test_products.name == "Iphone 15"
        assert test_products.description == "512GB, Gray space"
        assert test_products.price == 31000.0
        assert test_products.quantity == 14
