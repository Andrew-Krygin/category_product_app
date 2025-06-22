import json
from pathlib import Path
from typing import Any

from models.category import Category
from models.product import Product

BASE_DIR = Path(__file__).resolve().parent.parent / "data"
FILE_PATH = BASE_DIR / "products.json"


def read_file(file_path: Path) -> list[dict] | Any:
    """
    Функция читает json файл и возвращает список словарей.
    :param file_path: Путь к файлу json.
    :return: Список словарей.
    """
    try:
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        raise
    except json.JSONDecodeError:
        raise
    except Exception:
        raise


def load_categories_from_file() -> list[Category]:
    """
    Функция реализует подгрузку данных по категориям и товарам из файла JSON.
    :return: Список категорий.
    """
    data = read_file(FILE_PATH)

    category_list = []
    for category in data:
        name = category.get("name", "")
        description = category.get("description", "")
        products = category.get("products")

        products_list = []

        if isinstance(products, list):
            for product in products:
                product_obj = Product(
                    name=product.get("name"),
                    description=product.get("description"),
                    price=product.get("price"),
                    quantity=product.get("quantity"),
                )
                products_list.append(product_obj)

        category_list.append(Category(name, description, products_list))
    return category_list
