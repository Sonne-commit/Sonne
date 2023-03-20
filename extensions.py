import json
import requests
from config import keys


class ConvertionException(Exception):
    pass


class APIException:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(
                f'Нельзя перевести одинаковые валюты {base}.')

        try:

            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не смог обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не смог обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не смог обработать количество {amount}')

        if amount < 0:
            raise ConvertionException(f'Количество должно быть положительным числом {amount}. Уберите "-"')

        r = requests.get(
            f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = amount * json.loads(r.content)[keys[base]]
        return total_base


class DeclensionByCases():
    def __init__(self, word, num):
        self.word = word
        self.num = num

    def incline(self):
        if self.word != 'евро':
            if (2 <= self.num % 10 <= 4 and self.num % 100 not in [12, 13, 14]) or not self.num.is_integer():
                return 'рубля' if self.word == 'рубль' else self.word + 'a'
            if (self.num % 10 == 0 or 5 <= self.num % 10 <= 9 or 11 <= self.num % 100 <= 14) and self.num.is_integer():
                return 'рублей' if self.word == 'рубль' else self.word + 'ов'
        return self.word