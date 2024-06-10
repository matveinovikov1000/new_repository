from src.utils import read_file_operations
from src.masks import mask_card_number, mask_account_number


a = read_file_operations(filename="data/operations1.json")
print(a)
print(mask_card_number(1111222233334444))
print(mask_account_number(11112222333344445555))