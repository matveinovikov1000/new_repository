#Проект "Виджет"

##Описание:
Проект "Виджет" - это приложение на Python, позволяющее транслировать в личный кабинет клиента список последних 
успешных банковских операций. Дополнительно прект позволяет генирировать номера новых карт

##Установка:
Клонируйте репозиторий:
"""
git clone git@github.com:matveinovikov1000/new_repository.git
"""

##Тестирование:
Тестами покрыты не менее 80% кода

##Декораторы:
В проекте реализован декоратор, который выдает логи на тему штатно отработала функция или нет

##Модули masks.py и utils.py логируются в файлы masks.log и utils.log соответственно

##В модуле read_transactions.py реализовано чтение файлов transactions.csv и transactions_excel.xlsx

##Модуль selection_of_transactions.py включает в себя функции фильтрации списка транзакций

##Модуль main.py является главным и реализует в себе функцию фильтрации списка транзакций по выбранным параметрам с
использованием функций проекта