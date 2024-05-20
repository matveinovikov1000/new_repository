from typing import Iterable


def list_clean(entry_list: Iterable, mean_state: str = "EXECUTED") -> Iterable:
    """Функция, принимающая на вход список словарей, возвращающая список словарей, у которых ключ содержит переданное в
    функцию значение"""
    exit_list = []
    for dict_list in entry_list:
        if dict_list["state"] == mean_state:
            exit_list.append(dict_list)
    return exit_list


def list_sort(entry_list_sort: Iterable, reverse_list: bool = True) -> Iterable:
    """Функция, принимающая на вход список словарей, возвращающая отсоритированный по дате список словарей"""
    result_list_sort = sorted(entry_list_sort, key=lambda date_dict: date_dict["date"], reverse=reverse_list)
    return result_list_sort
