import sys
import os
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent.parent.resolve()
sys.path.insert(0, str(project_root))


# Should work now without any path modifications
from backend import db_helper

def test_fetch_expenses_for_date_aug_15():
    expenses = db_helper.fetch_expenses_for_date("2024-08-15")

    assert len(expenses) == 1
    assert expenses[0]["amount"] == 10.0
    assert expenses[0]["category"] == 'Shopping'
    assert expenses[0]['notes'] == 'Bought potatoes'

def test_fetch_expenses_for_date():
    expenses = db_helper.fetch_expenses_for_date("9999-08-15")

    assert len(expenses) == 0


def test_fetch_summary_expenses():
    summary = db_helper.fetch_summary_expenses('9999-08-02', "1994-08-03")
    assert len(summary) == 0
    