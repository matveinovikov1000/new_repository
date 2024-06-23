import json
import os

import requests
from dotenv import load_dotenv


def transaction_currency_conversion(transaction):
    """Показывает сумму транзакции, конвертирует USD и EUR в RUB"""
    currency_tran = transaction["operationAmount"]["currency"]["code"]
    amount_tran = transaction["operationAmount"]["amount"]
    if currency_tran == "RUB":
        return amount_tran
    elif currency_tran != "RUB":
        load_dotenv()
        payload = {}
        api_key = os.getenv("API_KEY")
        headers = {"apikey": api_key}
        url = (
            f"https://api.apilayer.com/exchangerates_data/convert?to={currency_tran}&from={"RUB"}&amount={amount_tran}"
        )
        response = requests.request("GET", url, headers=headers, data=payload)
        amount_api_tran = json.loads(response)
        return amount_api_tran["result"]
