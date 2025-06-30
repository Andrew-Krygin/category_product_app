from typing import ContextManager
from unittest.mock import patch

import pytest

from models.product import Product
from tests.tests_data.data_for_models import invalid_case_new_product, valid_case_new_product


@pytest.fixture
def test_products() -> Product:
    return Product("Iphone 15", "512GB, Gray space", 31000.0, 14)


class TestProduct:
    def test_init_product(self, test_products: Product) -> None:
        assert test_products.name == "Iphone 15"
        assert test_products.description == "512GB, Gray space"
        assert test_products.price == 31000.0
        assert test_products.quantity == 14

    def test__repr__(self, test_products: Product) -> None:
        ex_res = f"({test_products.name}, {test_products.price} руб. Остаток: {test_products.quantity})"
        assert test_products.__repr__() == ex_res

    def test_price(self, test_products: Product) -> None:
        assert test_products.price == 31000.0
        assert isinstance(test_products.price, float)

    @pytest.mark.parametrize(
        "input_price, ex_res",
        [
            (0, "Цена не должна быть нулевая или отрицательная\n"),
            (-23.0, "Цена не должна быть нулевая или отрицательная\n"),
        ],
    )
    def test_price_setter_zero_and_below_zero(
        self, capsys: pytest.CaptureFixture, test_products: Product, input_price: int | float, ex_res: str | float
    ) -> None:
        test_products.price = input_price
        captured = capsys.readouterr()
        assert captured.out == ex_res

    @pytest.mark.parametrize(
        "input_price, ex_res",
        [
            (37000.24, 37000.24),
            (31001.0, 31001.0),
        ],
    )
    def test_price_setter_more_established(self, test_products: Product, input_price: float, ex_res: float) -> None:
        test_products.price = input_price
        assert test_products.price == ex_res

    def test_price_setter_more_zero_bellow_established_y(self, test_products: Product) -> None:
        with patch("builtins.input", return_value="y") as mock_input:
            test_products.price = 29000.0
            assert test_products.price == 29000.0
            mock_input.assert_called()

    def test_price_setter_more_zero_bellow_established_n(self, test_products: Product) -> None:
        with patch("builtins.input", return_value="n") as mock_input:
            test_products.price = 15500.0
            assert test_products.price == 31000.0
            mock_input.assert_called()

    @pytest.mark.parametrize(
        "input_new_prod, ex_res, expectation",
        [
            valid_case_new_product,
            invalid_case_new_product,
        ],
    )
    def test_new_product(
        self, test_products: Product, input_new_prod: dict, ex_res: Product | None, expectation: ContextManager
    ) -> None:
        with expectation:
            result = test_products.new_product(input_new_prod)
            assert result == ex_res
