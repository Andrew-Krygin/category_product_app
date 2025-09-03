import pytest

from models.category import Category
from models.product import LawnGrass, Product, Smartphone
from tests.tests_data.data_for_models import list_products


class TestCategory:
    def test_init_category(self, sample_category: Category) -> None:
        assert isinstance(sample_category, Category)
        assert sample_category.name == "Смартфоны"
        assert sample_category.description == "Смартфоны, лучшее что придумало человечество."
        assert sample_category.cnt_categories == 1
        assert sample_category.cnt_products == len(list_products)

    def test_products(self, sample_category: Category) -> None:
        assert sample_category.products == list_products
        assert isinstance(sample_category.products, list)

    def test_add_smartphone(self, sample_category: Category) -> None:
        smartphone = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
        sample_category.add_product(smartphone)
        assert sample_category.cnt_products == 4

    def test_add_lawn_grass(self, sample_category: Category) -> None:
        grass = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
        sample_category.add_product(grass)
        assert sample_category.cnt_products == 4

    @pytest.mark.parametrize(
        "input_data",
        [
            Category(
                "Смартфоны",
                "Смартфоны, как средство не только "
                "коммуникации, но и получения дополнительных функций для удобства жизни",
                [
                    Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
                ],
            ),
        ],
    )
    def test_add_product_exception(self, sample_category: Category, input_data: Category) -> None:
        with pytest.raises(TypeError):
            sample_category.add_product(input_data)  # type: ignore

    def test_add_products(self, sample_category: Category) -> None:
        sample_category.add_product(Product("Banana", "Ripe banana", 2.0, 20))
        assert sample_category.cnt_products == 4

    @pytest.mark.parametrize(
        "input_data, ex_res, ex_cnt, ex_price",
        [
            (Product("Banana", "Ripe banana", 2.0, 20), False, 20, 2.0),
            (Product("Iphone 15", "512GB, Gray space", 210000.0, 8), True, 16, 210000.0),
            (Product("Xiaomi Redmi Note 11", "1024GB, Синий", 37000.0, 14), True, 28, 37000.0),
        ],
    )
    def test_product_exists(
        self, sample_category: Category, input_data: Product, ex_res: bool, ex_cnt: int, ex_price: float
    ) -> None:
        assert sample_category.product_exists(input_data) == ex_res

        found_product = next((prod for prod in sample_category.products if prod.name == input_data.name), None)
        if ex_res:
            assert found_product is not None
            assert found_product.quantity == ex_cnt
            assert found_product.price == ex_price
        else:
            assert found_product is None

    def test__str__(self, sample_category: Category) -> None:
        ex_res = "Смартфоны, количество продуктов: 27."
        assert sample_category.__str__() == ex_res

    def test_middle_price(self, sample_category: Category) -> None:
        middle_price = sample_category.middle_price
        assert middle_price == 140333.33

    def test_middle_price_empty_list_products(self) -> None:
        cat1 = Category("Смартфоны", "Смартфоны, лучшее что придумало человечество.", [])
        middle_price = cat1.middle_price
        assert middle_price == 0.0
