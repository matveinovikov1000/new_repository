def filter_by_currency(transactions, currency_selection):
    """Функция, фильтрующая список оперций по выбранной валюте"""
    descriptions = []
    for transaction in transactions:
        try:
            if transaction["operationAmount"]["currency"]["code"] == currency_selection:
                descriptions.append(transaction)
        except KeyError:
            pass
    return descriptions


def filter_by_currency_csv_xlsx(transactions, currency_selection):
    """Функция, фильтрующая список операций из файлов csv и xlsx по выбранной валюте"""
    descriptions = []
    for transaction in transactions:
        try:
            if transaction["currency_code"] == currency_selection:
                descriptions.append(transaction)
        except KeyError:
            pass
    return descriptions


def transaction_descriptions(transactions):
    """Функция, возвращающая описание каждой операции из списка"""
    description_transaction = (x["description"] for x in transactions)
    return description_transaction


def card_number_generator(start=1, stop=9999999999999999):
    """Функция, генерирующая номер карты"""
    while True:
        result = f"{start:016d}"
        yield result[:4] + " " + result[4:8] + " " + result[8:12] + " " + result[12:]
        start += 1
        if start == stop + 1:
            break
