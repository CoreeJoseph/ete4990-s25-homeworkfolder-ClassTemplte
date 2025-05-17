import datetime
import random

ALL_CURRENCIES = [
    "EUR", "GBP", "USD", "DZD", "AUD", "BWP", "BND", "CAD", "CLP", "CNY",
    "COP", "CZK", "DKK", "HUF", "ISK", "INR", "IDR", "ILS", "KZT", "KRW", "KWD",
    "LYD", "MYR", "MUR", "NPR", "NZD", "NOK", "OMR", "PKR", "PLN", "QAR", "RUB",
    "SAR", "SGD", "ZAR", "LKR", "SEK", "CHF", "THB", "TTD"
]

BASE_CURRENCY = random.choice([c for c in ALL_CURRENCIES if c not in ["USD", "EUR", "GBP"]])
START_DATE = datetime.date(2011, 5, 4)
END_DATE = datetime.date.today()

MAX_THREADS = 10
BASE_FOLDER = f"data/{BASE_CURRENCY}"