from src.masks import mask_account_number, mask_card_number


def test_mask_card_number(card_number):
    assert mask_card_number(card_number) == "1111 22** **** 4444"


def test_mask_account_number(account_number):
    assert mask_account_number(account_number) == "**5555"
