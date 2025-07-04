import pytest

from models.category import Category
from models.category_product_iterator import CategoryProductIterator


class TestCategoryProductIterator:
    def test_init_category_product_iterator(self, sample_category: Category) -> None:
        example_1 = CategoryProductIterator(sample_category)

        assert example_1._category == sample_category
        assert example_1._products == sample_category.products
        assert example_1._index == 0

    def test_valid_category_product_iterator(self, sample_category: Category) -> None:
        cat_iterator = CategoryProductIterator(sample_category)
        assert list(cat_iterator) == sample_category.products

    def test_exception_category_product_iterator(self) -> None:
        with pytest.raises(StopIteration):
            next(CategoryProductIterator(Category("Канцтовары", "Канцтовары для школы", [])))
