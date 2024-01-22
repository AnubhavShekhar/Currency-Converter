from dotenv import load_dotenv
from icecream import ic
import os
import requests

load_dotenv()

"""
Setting API key
"""

API_TOKEN = os.getenv("API_KEY")
URL = f"{os.getenv("BASE_URL")}{API_TOKEN}"

"""
Dictionary of currencies
"""

CURRENCIES = {'AUD': 'Australian Dollar',
                'BGN': 'Bulgarian Lev',
                'BRL': 'Brazilian Real',
                'CAD': 'Canadian Dollar',
                'CHF': 'Swiss Franc',
                'CNY': 'Chinese Yuan',
                'CZK': 'Czech Republic Koruna',
                'DKK': 'Danish Krone',
                'EUR': 'Euro',
                'GBP': 'British Pound Sterling',
                'HKD': 'Hong Kong Dollar',
                'HRK': 'Croatian Kuna',
                'HUF': 'Hungarian Forint',
                'IDR': 'Indonesian Rupiah',
                'ILS': 'Israeli New Sheqel',
                'INR': 'Indian Rupee',
                'ISK': 'Icelandic KrÃ³na',
                'JPY': 'Japanese Yen',
                'KRW': 'South Korean Won',
                'MXN': 'Mexican Peso',
                'MYR': 'Malaysian Ringgit',
                'NOK': 'Norwegian Krone',
                'NZD': 'New Zealand Dollar',
                'PHP': 'Philippine Peso',
                'PLN': 'Polish Zloty',
                'RON': 'Romanian Leu',
                'RUB': 'Russian Ruble',
                'SEK': 'Swedish Krona',
                'SGD': 'Singapore Dollar',
                'THB': 'Thai Baht',
                'TRY': 'Turkish Lira',
                'USD': 'US Dollar',
                'ZAR': 'South African Rand'}

"""
Converting base currency into different currencies
"""

def convert_currency(base):
    # getting tickers and creating url request
    currencies = ",".join(CURRENCIES.keys())
    url = f"{URL}&base_currency={base}&currencies={currencies}"

    try:
        # Fetching the exchange rates
        response = requests.get(url)
        data = response.json()
        return data["data"]

    except:
        print("Invalid currency")
        return None

while True:
    base = input("Enter the base currency (q for quit):").upper()

    if base == "Q":
        break
    
    data = convert_currency(base)
    if not data:
        continue

    try:
        value = float(input("Enter the value:"))
        if value:
            for curr, rate in data.items():
                data[curr] = round(rate * value, 4)

    except Exception as e:
        print("no value entered.. Printing the EXCHANGE RATES!")

    del data[base]
    ic(data)