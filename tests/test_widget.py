from src.widget import mask_account_card_number
from src.widget import date_format


def test_mask_account_card_number(name_account_number):
    assert mask_account_card_number(name_account_number) == "Счет **9589"


def test_date_format(input_date):
    assert date_format(input_date) == "11.07.2018"
