def mask_card_number(card_number: int) -> str:
    """Функция, которая маскирует номер карты"""
    str_card_number = str(card_number)
    result_card_number = (
        str_card_number[0:4]
        + " "
        + str_card_number[4:6]
        + "**"
        + " "
        + "****"
        + " "
        + str_card_number[12:]
    )
    return result_card_number


def mask_account_number(account_number: int) -> str:
    """Функция, которая маскирует номер счёта"""
    str_account_number = str(account_number)
    result_card_number = "**" + str_account_number[-4:]
    return result_card_number
