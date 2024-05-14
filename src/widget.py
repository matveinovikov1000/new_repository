from src.masks import mask_card_number
from src.masks import mask_account_number


def mask_account_card_number(name_number_account_card: str) -> str:
    """Функция, принимающая наименование карты/счёта и её/его номер и возвращат наименование с маскированным номером"""
    new_mask_card_number = ""
    new_mask_account_number = ""
    name_card_one = ""
    name_card_two = ""
    name_account = ""
    number_account_card = name_number_account_card.split()

    if len(number_account_card[-1]) > 16:
        new_mask_account_number += mask_account_number(int(number_account_card[-1]))
        name_account += number_account_card[0]
        return name_account + " " + new_mask_account_number
    elif len(number_account_card[-1]) == 16:
        new_mask_card_number += mask_card_number(int(number_account_card[-1]))
        if len(number_account_card) == 2:
            name_card_one += number_account_card[0]
        elif len(number_account_card) == 3:
            name_card_one += number_account_card[0]
            name_card_two += number_account_card[1]
    return name_card_one + " " + name_card_two + " " + new_mask_card_number


def date_format(entry_date: str) -> str:
    """Функция, которая преобразует дату в читабельный формат"""
    date_list = entry_date[0:10].split("-")
    new_date = date_list[2] + "." + date_list[1] + "." + date_list[0]
    return new_date
