from typing import Any, Iterator

from models.category import Category


class CategoryProductIterator:
    """
    Класс для перебора товаров одной категории.
    """

    def __init__(self, category: Category) -> None:
        """
        Инициализация нового объекта класса CategoryProductIterator.
        :param category: Объект класса Category.
        """
        if not isinstance(category, Category):
            raise ValueError("Объект должен быть класса Category.")
        self._category = category
        self._products = category.products
        self._index = 0

    def __iter__(self) -> Iterator:
        """
        Возвращает итератор.
        :return: Iterator.
        """
        return self

    def __next__(self) -> Any:
        """
        Возвращает следующий товар категории.
        :return: Товар категории.
        """
        if self._index < len(self._products):
            item = self._products[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration
