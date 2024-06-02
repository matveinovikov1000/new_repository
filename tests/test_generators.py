from src.generators import filter_by_currency
from src.generators import card_number_generator


def test_filter_by_currency(transactions, currency_selection):
    expected_result = [939719570, 142264268, 895315941]
    result_list = []
    filter(lambda currency: currency["operationAmount"]["currency"]["code"] == currency_selection, transactions)
    usd_transactions = filter_by_currency(transactions, "USD")

    for _ in range(3):
        result_list.append(next(usd_transactions)["id"])

    assert result_list == expected_result


def test_transaction_descriptions(transactions):
    expected_result_one = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    result_one = list((x["description"] for x in transactions))
    assert result_one == expected_result_one


def test_card_number_generator():
    generator = card_number_generator()
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
