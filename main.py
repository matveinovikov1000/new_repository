import sys

from src.generators import filter_by_currency, filter_by_currency_csv_xlsx
from src.processing import list_clean, list_sort
from src.read_transactions import read_transactions_csv, read_transactions_excel
from src.selection_of_transactions import select_description
from src.utils import read_file_operations
from src.widget import date_format, mask_account_card_number


def main():
    """Главная функция, в которой реализована фильтрация списка странзакций по выбранным критериям"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    user_input_format = int(
        input(
            """Выберите необходимый пункт меню:
            1. Получить информацию о транзакциях из JSON-файла
            2. Получить информацию о транзакциях из CSV-файла
            3. Получить информацию о транзакциях из XLSX-файла"""
        )
    )

    if user_input_format == 1:
        get_read = read_file_operations(filename="data/operations.json")
        print("Для обработки выбран JSON-файл")
    elif user_input_format == 2:
        get_read = read_transactions_csv(filename="data/transactions.csv")
        print("Для обработки выбран csv-файл")
    elif user_input_format == 3:
        get_read = read_transactions_excel(filename="data/transactions_excel.xlsx")
        print("Для обработки выбран excel-файл")
    else:
        print("Такого варианта нет")
        sys.exit()

    user_input_status_up = str(
        input(
            """Введите статус, по которому необходимо выполнить фильтрацию.
                Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
        )
    ).upper()

    if user_input_status_up == "EXECUTED" or user_input_status_up == "CANCELED" or user_input_status_up == "PENDING":
        print(f"Операции отфильтрованы по статусу {user_input_status_up}")
    elif user_input_status_up != "EXECUTED" or user_input_status_up != "CANCELED" or user_input_status_up != "PENDING":
        print("Такого варианта нет")
        sys.exit()

    state_sort = list_clean(entry_list=get_read, mean_state=user_input_status_up)
    date_sort_low = str(input("Отсортировать операции по дате? Да/Нет")).lower()

    if date_sort_low == "да":
        date_sort_reverse_low = str(input("Отсортировать по возрастанию или убыванию?")).lower()

        if date_sort_reverse_low == "по убыванию":
            date_sort_reverse_func = list_sort(entry_list_sort=state_sort, reverse_list=True)
        elif date_sort_reverse_low == "по возрастанию":
            date_sort_reverse_func = list_sort(entry_list_sort=state_sort, reverse_list=False)

    elif date_sort_low == "нет":
        date_sort_reverse_func = state_sort
    else:
        print("Такого варианта нет")
        sys.exit()

    date_currency_low = str(input("Выводить только рублевые тразакции? Да/Нет")).lower()

    if user_input_format == 1:
        if date_currency_low == "да" and date_sort_low == "нет":
            date_currency_func = filter_by_currency(transactions=state_sort, currency_selection="RUB")
        elif date_currency_low == "да" and date_sort_low == "да":
            date_currency_func = filter_by_currency(transactions=date_sort_reverse_func, currency_selection="RUB")
        elif date_currency_low == "нет":
            date_currency_func = date_sort_reverse_func
        else:
            print("Такого варианта нет")
            sys.exit()

    elif user_input_format != 1:
        if date_currency_low == "да" and date_sort_low == "нет":
            date_currency_func = filter_by_currency_csv_xlsx(transactions=state_sort, currency_selection="RUB")
        elif date_currency_low == "да" and date_sort_low == "да":
            date_currency_func = filter_by_currency_csv_xlsx(
                transactions=date_sort_reverse_func, currency_selection="RUB"
            )
        elif date_currency_low == "нет":
            date_currency_func = date_sort_reverse_func
        else:
            print("Такого варианта нет")
            sys.exit()

    date_description_low = str(
        input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    ).lower()

    if date_description_low == "да":
        user_input_description = input("Введите слово")
        date_description_low_func = select_description(date_currency_func, user_input_description)
    elif date_description_low == "нет":
        date_description_low_func = date_currency_func
    else:
        print("Такого варианта нет")
        sys.exit()

    if date_description_low_func == {}:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        sys.exit()

    print(
        f"Распечатываю итоговый список транзакций...\n"
        f"Всего банковских операций в выборке: {len(date_description_low_func)}\n"
    )

    if user_input_format == 1:
        for i in date_description_low_func:
            date = date_format(i["date"])
            description_oper = i["description"]
            mask_from = mask_account_card_number(i["from"])
            mask_to = mask_account_card_number(i["to"])
            amount = i["operationAmount"]["amount"]
            currency = i["operationAmount"]["currency"]["name"]

            print(f"{date} {description_oper}\n{mask_from}->{mask_to}\nСумма: {amount} {currency}\n")
    else:
        for i in date_description_low_func:
            date = date_format(i["date"])
            description_oper = i["description"]
            mask_from = mask_account_card_number(i["from"])
            mask_to = mask_account_card_number(i["to"])
            amount = i["amount"]
            currency = i["currency_name"]

            print(f"{date} {description_oper}\n{mask_from}->{mask_to}\nСумма: {amount} {currency}\n")


print(main())
