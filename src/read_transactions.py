import csv
import json

import pandas as pd


def read_transactions_csv(filename):
    """Считывание финансовых операций из файла .csv"""
    with open(filename, "r", encoding="utf8") as file:
        reader_csv = csv.reader(file, delimiter=";")
        header = next(reader_csv)
        result = []
        for row in reader_csv:
            row_dict = dict()
            for key, item in enumerate(header):
                row_dict[item] = row[key]
            result.append(row_dict)
    return result


def read_transactions_excel(filename):
    """Считывание финансовых операций из файла .xlsx"""
    reader_excel = pd.read_excel("data/transactions_excel.xlsx").to_json(orient="records", indent=4, force_ascii=False)
    return json.loads(reader_excel)
