import pytest

from models.category import Category
from models.order import Order
from models.product import Product
from tests.tests_data.data_for_models import category_for_order, error_message_1, error_message_2


class TestOrder:
    def test_init_order(self, sample_order: Order) -> None:
        assert sample_order.name == "Заказ №1"
        assert sample_order.description == "Покупка смартфона"
        assert sample_order.category.name == "Смартфоны"
        assert sample_order.product_name == "Iphone 15"
        assert sample_order.quantity == 2

    def test_order_initialization_finds_correct_product(self, sample_order: Order) -> None:
        res = sample_order.product
        assert res == Product("Iphone 15", "512GB, Gray space", 210000.0, 6)

    def test_order_initialization_raises_value_error_if_product_not_found(self) -> None:
        with pytest.raises(ValueError, match=error_message_1):
            assert Order(
                "Заказ №2", "Покупка телефона", Category("Смартфоны", "Хорошие смартфоны", []), "Iphone 15", 2
            )

    def test_order_raises_when_quantity_too_large(self) -> None:
        with pytest.raises(ValueError, match=error_message_2):
            assert Order("Заказ №2", "Покупка телефона", category_for_order, "Iphone 15", 14)

    def test__str__order(self, capsys: pytest.CaptureFixture, sample_order: Order) -> None:
        print(sample_order)
        captured = capsys.readouterr()
        assert captured.out.strip() == (
            "Заказ: Заказ №1\n"
            "Описание: Покупка смартфона\n"
            "Товар: Iphone 15\n"
            "Количество куплено: 2\n"
            "Стоимость: 420000.0 руб.\n"
            "Остаток на складе: 6 шт."
        )
