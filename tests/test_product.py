from typing import Any, ContextManager
from unittest.mock import patch

import pytest

from models.category import Category
from models.product import Product
from tests.tests_data.data_for_models import invalid_case_new_product, valid_case_new_product


class TestProduct:
    def test_init_product(self, sample_products: Product) -> None:
        assert sample_products.name == "Iphone 15"
        assert sample_products.description == "512GB, Gray space"
        assert sample_products.price == 31000.0
        assert sample_products.quantity == 14

    def test__str__(self, sample_products: Product) -> None:
        ex_res = "Iphone 15, 31000.0 руб. Остаток: 14"
        assert sample_products.__str__() == ex_res

    def test_price(self, sample_products: Product) -> None:
        assert sample_products.price == 31000.0
        assert isinstance(sample_products.price, float)

    @pytest.mark.parametrize(
        "input_price, ex_res",
        [
            (0, "Цена не должна быть нулевая или отрицательная\n"),
            (-23.0, "Цена не должна быть нулевая или отрицательная\n"),
        ],
    )
    def test_price_setter_zero_and_below_zero(
        self, capsys: pytest.CaptureFixture, sample_products: Product, input_price: int | float, ex_res: str | float
    ) -> None:
        sample_products.price = input_price
        captured = capsys.readouterr()
        assert captured.out == ex_res

    @pytest.mark.parametrize(
        "input_price, ex_res",
        [
            (37000.24, 37000.24),
            (31001.0, 31001.0),
        ],
    )
    def test_price_setter_more_established(self, sample_products: Product, input_price: float, ex_res: float) -> None:
        sample_products.price = input_price
        assert sample_products.price == ex_res

    def test_price_setter_more_zero_bellow_established_y(self, sample_products: Product) -> None:
        with patch("builtins.input", return_value="y") as mock_input:
            sample_products.price = 29000.0
            assert sample_products.price == 29000.0
            mock_input.assert_called()

    def test_price_setter_more_zero_bellow_established_n(self, sample_products: Product) -> None:
        with patch("builtins.input", return_value="n") as mock_input:
            sample_products.price = 15500.0
            assert sample_products.price == 31000.0
            mock_input.assert_called()

    @pytest.mark.parametrize(
        "input_new_prod, ex_res, expectation",
        [
            valid_case_new_product,
            invalid_case_new_product,
        ],
    )
    def test_new_product(
        self, sample_products: Product, input_new_prod: dict, ex_res: Product | None, expectation: ContextManager
    ) -> None:
        with expectation:
            result = sample_products.new_product(input_new_prod)
            assert result == ex_res

    def test__repr__(self, sample_products: Product) -> None:
        ex_res = "Product('Iphone 15', '512GB, Gray space', 31000.0, 14)"
        assert sample_products.__repr__() == ex_res

    @pytest.mark.parametrize(
        "input_prod, ex_res",
        [
            (Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14), 868000.0),
            (Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5), 1334000.0),
        ],
    )
    def test__add__(self, sample_products: Product, input_prod: Product, ex_res: float) -> None:
        result = sample_products + input_prod
        assert result == ex_res

    @pytest.mark.parametrize(
        "input_data",
        [
            Category(
                "Вещи",
                "Вещи с барахолки",
                [
                    Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
                ],
            ),
            4,
            "",
            None,
        ],
    )
    def test_invalid_add(self, sample_products: Product, input_data: Any) -> None:
        with pytest.raises(TypeError):
            sample_products + input_data
