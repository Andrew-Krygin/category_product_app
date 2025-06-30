class Product:
    """Класс для представления продуктов."""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Инициализация нового продукта.
        :param name: Название продукта.
        :param description: Описание продукта.
        :param price: Цена продукта.
        :param quantity: Количество продукта.
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __repr__(self) -> str:
        """
        Возвращает строковое представление продукта.
        Формат: (название, цена руб., остаток)
        :return:Строка с информацией о продукте.
        """
        return f"({self.name}, {self.__price} руб. Остаток: {self.quantity})"

    def __eq__(self, other: object) -> bool:
        """
        Сравнивает два продукта на равенство по имени, описанию, цене и количеству.
        :param other: Объект для сравнения.
        :return: True, если продукты равны, иначе False.
        """
        return (
            isinstance(other, Product)
            and self.name == other.name
            and self.description == other.description
            and self.__price == other.__price
            and self.quantity == other.quantity
        )

    @property
    def price(self) -> float:
        """
        Возвращает цену продукта.
        :return: Цена продукта.
        """
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        """
        Устанавливает новую цену продукта с проверкой.
        Если новая цена меньше или равна нулю, выводится предупреждение и цена не изменяется.
        Если новая цена меньше текущей, пользователь подтверждает изменение вручную.
        :param price: Цена.
        :return: None.
        """
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif self.__price > price:
            choice = input(f"Вы действительно хотите установить {price} руб. в качестве цены(y/n): ")
            if choice.strip().lower() == "y":
                self.__price = price
        else:
            self.__price = price

    @classmethod
    def new_product(cls, new_product: dict) -> "Product":
        """
        Создаёт и возвращает новый экземпляр класса Product на основе словаря с параметрами.
        :param new_product: Словарь с ключами 'name', 'description', 'price', 'quantity'.
        :return: Объект класса Product.
        """
        name = new_product.get("name")
        description = new_product.get("description")
        price = new_product.get("price")
        quantity = new_product.get("quantity")

        if (name is None) or (description is None) or (price is None) or (quantity is None):
            raise ValueError("A key required to create an object of class Product is missing.")
        return cls(name, description, price, quantity)
