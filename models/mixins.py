from typing import Any


class MixinLogToConsole:
    """Выводит в консоль информацию о том, от какого класса и с какими параметрами был создан объект."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        print(f"{self.__class__.__name__}({', '.join(map(str, self.__dict__.values()))})")
