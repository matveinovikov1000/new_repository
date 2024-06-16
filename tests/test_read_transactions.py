from unittest.mock import patch

from src.read_transactions import read_transactions_csv, read_transactions_excel


@patch("pd.read_csv")
def test_read_transactions_csv(mock):
    mock.return_value.shape = ("1000", "1")
    assert read_transactions_csv == ("1000", "1")


@patch("pd.read_excel")
def test_read_transactions_excel(mock):
    mock.return_value.shape = ("1000", "9")
    assert read_transactions_excel == ("1000", "9")
