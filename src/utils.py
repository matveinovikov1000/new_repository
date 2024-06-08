import json


def read_file_operations(filename):
    """Возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(filename, encoding="utf8") as file:
            transactions = json.load(file)
        if type(transactions) is list:
            return transactions
        else:
            return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
