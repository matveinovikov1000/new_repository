from unittest.mock import patch

from src.external_api import transaction_currency_conversion


@patch("amount_api_tran")
def test_transaction_currency_conversion(mock):
    mock.return_value = "100"
    assert transaction_currency_conversion == "100"
