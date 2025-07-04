# category_product_app

## Описание проекта
Проект создан для проработки использования классов и объектов на основе популярной темы e-commerce.


## Структура проекта
- **models/category**: Модуль содержит определение класса Category с атрибутами и подсчётом категорий и товаров.
- **models/product**: Модуль содержит определение класса Product с основными свойствами товара.
- **src/loader**: Модуль для чтения данных из JSON-файла и создания объектов Category и Product.
- **data/**: Директория для хранения JSON-файла.
- **tests/**: Папка с тестами для проверки корректности работы классов и функций.


## Установка
##### Для пользователя:
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Andrew-Krygin/category_product_app.git
   ```
   
2. Перейдите в каталог проекта:
   ```bash
   cd category_product_app
   ```
   
3. Установите зависимости с помощью Poetry:
   ```bash
   poetry install
   ```
   

##### Для разработчика:
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Andrew-Krygin/category_product_app.git
   ```
   
2. Перейдите в каталог проекта:
   ```bash
   cd category_product_app
   ```
   
3. Установите зависимости с помощью Poetry:
   ```bash
   poetry install
   ```
   
## Пример использования
Будут добавлены позднее.


## Тестирование
Проект использует pytest для модульного тестирования и pytest-cov для оценки покрытия кода. 

- Установите необходимые зависимости для разработки:
   ```bash
   poetry add --dev pytest pytest-cov
   ```

### Запуск тестов
- Для запуска всех тестов:
   ```bash
   poetry run pytest
   ```

- Для более подробного вывода:
   ```bash
   poetry run pytest -v
   ```

### Проверка покрытия кода
- Запуск с отображением процента покрытия:
   ```bash
   poetry run pytest --cov=src
   ```

- Для генерации HTML-отчёта покрытия:
   ```bash
   poetry run pytest --cov=src --cov=models --cov-report=html
   ```

HTML-отчёт будет доступен по пути `htmlcov/index.html`.

### Структура тестов
- Все тесты расположены в директории `tests/`.
- Тестовые кейсы вынесены в папку `tests/tests_data/`.
- Покрываются модули `models/category`, `models/product`.

## Авторы
- [Andrew Krygin](https://github.com/Andrew-Krygin)
