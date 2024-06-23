import re
from collections import Counter


def select_description(data_transactions, user_input):
    """Поиск операций по описанию"""
    user_data_transact = []
    for transaction in data_transactions:
        try:
            match = re.search(user_input.lower(), transaction["description"].lower())
            if match:
                user_data_transact.append(transaction)
        except KeyError:
            pass
    return user_data_transact


def search_descriptions(data_transactions):
    """Формирование списка категорий"""
    descriptions = []
    for transaction in data_transactions:
        try:
            if transaction["description"] not in descriptions:
                descriptions.append(transaction["description"])
        except KeyError:
            pass
    return descriptions


def transaction_counting(data_transactions, search_descriptions):
    """Подсчёт операций в разрезе категорий"""
    list_search_descriptions = []
    search_list = search_descriptions(data_transactions)
    for transaction in data_transactions:
        try:
            if transaction["description"] in search_list:
                list_search_descriptions.append(transaction["description"])
        except KeyError:
            pass
    quantity_search_descriptions = Counter(list_search_descriptions)
    return quantity_search_descriptions
