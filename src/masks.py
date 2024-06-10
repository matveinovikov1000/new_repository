import logging


logger_mask = logging.getLogger(__name__)
file_handler_mask = logging.FileHandler("logs/masks.log", "w", encoding="utf8")
file_formatter_mask = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler_mask.setFormatter(file_formatter_mask)
logger_mask.addHandler(file_handler_mask)
logger_mask.setLevel(logging.DEBUG)


def mask_card_number(card_number: int) -> str:
    """Функция, которая маскирует номер карты"""
    str_card_number = str(card_number)
    logger_mask.info("Перевод в формат строки успешен")
    result_card_number = (
        str_card_number[0:4] + " " + str_card_number[4:6] + "**" + " " + "****" + " " + str_card_number[12:]
    )
    logger_mask.info("Номер карты замаскирован")
    return result_card_number


def mask_account_number(account_number: int) -> str:
    """Функция, которая маскирует номер счёта"""
    str_account_number = str(account_number)
    logger_mask.info("Перевод в формат строки успешен")
    result_card_number = "**" + str_account_number[-4:]
    logger_mask.info("Номер счёта замаскирован")
    return result_card_number
