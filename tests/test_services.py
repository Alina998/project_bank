import json
from pathlib import Path

from src.services import simple_search
from src.utils import read_excel

file_path = str(Path(__file__).resolve().parent.parent) + "\\data\\operations.xlsx"
my_list = read_excel(file_path)
empty_list = []


def test_services_works():
    """Тестирование функции простой поиск в обычных условиях"""
    assert simple_search(my_list, "Ozon.ru") == json.dumps([
        {
            "Дата платежа": "31.12.2021",
            "Статус": "OK",
            "Сумма платежа": -564.0,
            "Валюта платежа": "RUB",
            "Категория": "Различные товары",
            "Описание": "Ozon.ru",
            "Номер карты": "*5091"
        },
        {
            "Дата платежа": "20.12.2021",
            "Статус": "OK",
            "Сумма платежа": 421.0,
            "Валюта платежа": "RUB",
            "Категория": "Различные товары",
            "Описание": "Ozon.ru",
            "Номер карты": "*7197"
        },
        {
            "Дата платежа": "14.12.2021",
            "Статус": "OK",
            "Сумма платежа": -421.0,
            "Валюта платежа": "RUB",
            "Категория": "Различные товары",
            "Описание": "Ozon.ru",
            "Номер карты": "*7197"
        },
        {
            "Дата платежа": "21.10.2021",
            "Статус": "OK",
            "Сумма платежа": -119.0,
            "Валюта платежа": "RUB",
            "Категория": "Различные товары",
            "Описание": "Ozon.ru",
            "Номер карты": "*7197"
        },
        {
            "Дата платежа": "04.10.2020",
            "Статус": "OK",
            "Сумма платежа": -750.0,
            "Валюта платежа": "RUB",
            "Категория": "Различные товары",
            "Описание": "Ozon.ru",
            "Номер карты": "*7197"
        }
    ], indent=4,
        ensure_ascii=False, )


def test_services_empty_attribute():
    """Тестирование функции простой поиск, с пустыми атрибутами """
    assert simple_search(empty_list, "Ozon.ru") == json.dumps([], indent=4,
                                                              ensure_ascii=False, )
    assert simple_search(my_list, "") == []
