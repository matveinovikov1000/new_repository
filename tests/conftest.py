import pytest


@pytest.fixture
def card_number():
    return 1111222233334444


@pytest.fixture
def account_number():
    return 11112222333344445555


@pytest.fixture
def name_account_number():
    return "Счет 64686473678894779589"


@pytest.fixture
def input_date():
    return "2018-07-11T02:26:18.671407"
