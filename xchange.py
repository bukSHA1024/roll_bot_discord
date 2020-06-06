import requests

class Exchange:
    state = "https://www.cbr-xml-daily.ru/daily_json.js"

    def bank(self, state):
        state = Exchange.state
        data = requests.get(link)
        valute = data.json()['Valute']
        return valute

class RUB(Exchange):
    def __init__(self, rub):
        self.rub = rub

    def exchange_rub_to_eur(self):
        bank = self.bank(Exchange.state)
        rate = bank['EUR']['Value']
        return self.rub * rate

    def exchange_rub_to_usd(self):
        bank = self.bank(Exchange.state)
        rate = bank['USD']['Value']
        return self.rub * rate