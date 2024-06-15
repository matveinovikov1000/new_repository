import pandas as pd


def read_transactions_csv(filename):
    """Считывание финансовых операций из файла .csv"""
    reader_csv = pd.read_csv("data/transactions.csv")
    return reader_csv


def read_transactions_excel(filename):
    """Считывание финансовых операций из файла .xlsx"""
    reader_excel = pd.read_excel("data/transactions_excel.xlsx")
    return reader_excel
