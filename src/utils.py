import json
import logging


logger_operat = logging.getLogger(__name__)
file_handler_operat = logging.FileHandler("logs/utils.log", "w", encoding="utf8")
file_formatter_operat = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler_operat.setFormatter(file_formatter_operat)
logger_operat.addHandler(file_handler_operat)
logger_operat.setLevel(logging.DEBUG)


def read_file_operations(filename):
    """Возвращает список словарей с данными о финансовых транзакциях"""
    try:
        logger_operat.info("Открытие файла")
        with open(filename, encoding="utf8") as file:
            transactions = json.load(file)
        logger_operat.info("Сравнение объекта со списком")
        if type(transactions) is list:
            return transactions
        else:
            return []
    except FileNotFoundError:
        logger_operat.warning("Файл не найден")
        return []
    except json.JSONDecodeError:
        logger_operat.warning("Файл пуст")
        return []
