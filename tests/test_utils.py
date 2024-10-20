import os
from pathlib import Path
from unittest.mock import Mock, patch

from dotenv import load_dotenv

from src.utils import currency_rates, for_each_card, get_price_stock, greetings, read_excel, top_five_transaction

file_path = str(Path(__file__).resolve().parent.parent) + "\\data\\operations.xlsx"
load_dotenv()
API_KEY_CUR = os.getenv("API_KEY_CUR")
my_list = read_excel(file_path)
empty_list = []


def test_greetings():
    """Тестирование функции приветствия"""
    assert greetings() == "Добрый день"


def test_for_each_card():
    """Тестирование функции создающей информацию по каждой карте, в обычном режиме"""
    assert for_each_card(my_list) == [{'last_digits': '7197', 'total_spent': 2504514.54, 'cashback': 25045.15},
                                      {'last_digits': '5091', 'total_spent': 18216.84, 'cashback': 182.17},
                                      {'last_digits': '4556', 'total_spent': 2103029.17, 'cashback': 21030.29},
                                      {'last_digits': '1112', 'total_spent': 46207.08, 'cashback': 462.07},
                                      {'last_digits': '5507', 'total_spent': 84000.0, 'cashback': 840.0},
                                      {'last_digits': '6002', 'total_spent': 69200.0, 'cashback': 692.0},
                                      {'last_digits': '5441', 'total_spent': 470854.8, 'cashback': 4708.55}]


def test_for_each_card_emp_att():
    """Тестирование функции создающей информацию по каждой карте, с пустым списком"""
    assert for_each_card(empty_list) == []


def test_top_five_transaction():
    """Тестирование функции для получения топ-5 транзакций по сумме платежа, в обычном режиме"""
    assert top_five_transaction(my_list) == [
        {'date': '01.09.2021', 'amount': 5990.0, 'category': 'Каршеринг', 'description': 'Ситидрайв'},
        {'date': '20.05.2021', 'amount': 8626.0, 'category': 'Бонусы', 'description': 'Компенсация покупки'},
        {'date': '14.05.2019', 'amount': 42965.94, 'category': 'Другое', 'description': 'ГУП ВЦКП ЖХ'},
        {'date': '30.04.2019', 'amount': 6100.0, 'category': 'Зарплата',
         'description': 'Пополнение. ООО "ФОРТУНА". Зарплата'},
        {'date': '23.04.2019', 'amount': 4518.0, 'category': 'Сервис', 'description': 'Kopirovalniy Centr'},
        {'date': '15.04.2019', 'amount': 6100.0, 'category': 'Зарплата',
         'description': 'Пополнение. ООО "ФОРТУНА". Аванс'},
        {'date': '21.03.2019', 'amount': 190044.51, 'category': 'Переводы',
         'description': 'Перевод Кредитная карта. ТП 10.2 RUR'},
        {'date': '28.08.2018', 'amount': 32999.0, 'category': 'Различные товары', 'description': 'SPb Trk Atmosfera'},
        {'date': '16.08.2018', 'amount': 3100.0, 'category': 'Транспорт', 'description': 'RigasStarptautiska autoos'},
        {'date': '19.04.2018', 'amount': 4292.8, 'category': 'Ж/д билеты', 'description': 'РЖД'},
        {'date': '10.03.2018', 'amount': 900.0, 'category': 'Кино', 'description': 'Каро Фильм'},
        {'date': '06.03.2018', 'amount': 10420.07, 'category': 'Частные услуги', 'description': 'YM*Login.Skolkovo'},
        {'date': '30.01.2018', 'amount': 2789.68, 'category': 'Супермаркеты', 'description': 'Перекрёсток'}]


def test_top_five_transaction_emp_att():
    """Тестирование функции для получения топ-5 транзакций по сумме платежа, с пустым списком"""
    assert top_five_transaction(empty_list) == []


@patch('requests.get')
def test_currency_rates(mock_get):
    """Тестирование функции вывода курса валют"""
    mock_response_usd = Mock()
    mock_response_usd.json.return_value = {"conversion_rates": {"RUB": 88.34}}
    mock_response_eur = Mock()
    mock_response_eur.json.return_value = {"conversion_rates": {"RUB": 97.8}}
    mock_get.side_effect = [mock_response_usd, mock_response_eur]

    result = currency_rates(['USD', 'EUR'])
    expected = [{"currency": "USD", "rate": 88.34}, {"currency": "EUR", "rate": 97.8}]
    assert result == expected


@patch("requests.get")
def test_fetch_stock_prices(mock_get):
    """Тестирование функции получения данных об акциях из списка S&P500"""

    mock_get.return_value.json.return_value = {"Global Quote": {"05. price": 210.00}}

    list_stocks = ["AAPL"]

    result = get_price_stock(list_stocks)
    expected = [
        {"stock": "AAPL", "price": 210.00},
    ]
    assert result == expected
