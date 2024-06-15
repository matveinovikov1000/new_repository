from src.utils import read_file_operations
from src.masks import mask_card_number, mask_account_number
from src.read_transactions import read_transactions_csv, read_transactions_excel


print(read_transactions_csv(filename="data/transactions.csv"))
print(read_transactions_excel(filename="data/transactions_excel.xlsx"))
#a = read_file_operations(filename="data/operations1.json")
#print(a)
#print(mask_card_number(1111222233334444))
#print(mask_account_number(11112222333344445555))