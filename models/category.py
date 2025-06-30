from models.product import Product


class Category:
    """
    Класс для представления категории продуктов.
    """

    # Атрибуты класса.
    cnt_categories = 0
    cnt_products = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        """
        Инициализация новой категории.
        :param name: Название категории.
        :param description: Описание категории.
        :param products: Список продуктов, относящихся к категории.
        """
        self.name = name
        self.description = description
        self.__products = products

        Category.cnt_categories += 1
        Category.cnt_products += len(self.__products)

    def __eq__(self, other: object) -> bool:
        """
        Сравнивает две категории на равенство по имени, описанию и продуктам.
        :param other:Объект для сравнения.
        :return:True, если категории равны, иначе False.
        """
        return (
            isinstance(other, Category)
            and self.name == other.name
            and self.description == other.description
            and self.__products == other.__products
        )

    @property
    def products(self) -> list:
        """
        Возвращает список продуктов категории.
        :return: Список продуктов.
        """
        return self.__products

    def add_product(self, product: Product) -> None:
        """
        Добавляет продукт в категорию и увеличивает счётчик продуктов.
        :param product: Продукт для добавления.
        :return: None.
        """
        self.__products.append(product)
        Category.cnt_products += 1

    def product_exists(self, new_product: Product) -> bool:
        """
        Проверяет, существует ли продукт с таким же именем в категории.
        Если существует, объединяет количество и обновляет цену по максимуму.
        :param new_product: Новый продукт для проверки.
        :return: True, если продукт найден и обновлён, иначе False.
        """
        for product in self.__products:
            if product.name == new_product.name:
                product.quantity += new_product.quantity
                if product.price != new_product.price:
                    product.price = max(product.price, new_product.price)

                return True
        return False
