from typing import Any


class ZeroQuantityError(Exception):
    """Вызывается, если пытаются добавить товар с нулевым количеством."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Инициализация атрибутов данных экземпляра класса ZeroQuantityError."""
        self.message = args[0] if args else "Количество товара-0"

    def __str__(self) -> str:
        """Возвращает строку с сообщением об исключении."""
        return self.message
