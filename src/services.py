import json
import logging

from src.decorators import decorator_search

logger = logging.getLogger("services.log")
file_handler = logging.FileHandler("services.log", "w")
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


@decorator_search
def simple_search(my_list: list, string_search: str):
    """Функция поиска по переданной строке"""
    result = []
    logger.info("Начало работы функции (simple_search)")
    for i in my_list:
        if string_search == '':
            return result
        elif (
                i["Описание"] == "nan"
                or type(i["Описание"]) is float
                or i["Категория"] == "nan"
                or type(i["Категория"]) is float
        ):
            continue
        elif string_search in i["Описание"] or string_search in i["Категория"]:
            result.append(i)

    logger.info("Конец работы функции (simple_search)")
    data_json = json.dumps(result,
                           indent=4,
                           ensure_ascii=False,
                           )

    return data_json
