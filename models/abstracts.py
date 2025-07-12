from abc import ABC, abstractmethod


# Абстрактный класс для модуля category.
class BaseEntity(ABC):
    """Абстрактный класс с общими свойствами (имя, описание) для категорий и заказов."""

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    @abstractmethod
    def __str__(self) -> str:
        pass


# Абстрактный класс для модуля product.
class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    quantity: int

    @abstractmethod
    def __add__(self, other: "BaseProduct") -> int | float:
        """Сложение продуктов."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Строковое представление продукта."""
        pass
