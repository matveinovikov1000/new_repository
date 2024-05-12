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

#print(mask_account_card_number("Счет 64686473678894779589"))