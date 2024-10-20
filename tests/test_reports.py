from pathlib import Path

import pytest

from src.reports import spending_by_category
from src.utils import read_excel

file_path = str(Path(__file__).resolve().parent.parent) + "\\data\\operations.xlsx"
result_read = read_excel(file_path)
result_spend = spending_by_category(result_read, "Переводы", date="31.12.2021")


@pytest.fixture
def fix_reports():
    return result_spend


def test_report(fix_reports):
    assert spending_by_category(result_read, "Переводы", date="31.12.2021") == fix_reports
    assert result_spend[0] == fix_reports[0]


def test_reports():
    assert spending_by_category(result_read, "Переводы") == []
    assert spending_by_category(result_read, "Красота") == []
    assert spending_by_category(result_read, "sdfsf") == []
