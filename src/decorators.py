import json
from typing import Any, Callable


def decorator_spending_by_category(func: Callable) -> Callable:
    """Логирует результат функции в файл по умолчанию decorator_spending_by_category.json"""

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        result = func(*args, **kwargs)
        with open("spending_by_category.json", "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)
        return result

    return wrapper


def decorator_search(func: Callable) -> Callable:
    """Логирует результат функции в файл по умолчанию decorator_search.json"""

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        result = func(*args, **kwargs)
        with open("search.json", "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)
        return result

    return wrapper
