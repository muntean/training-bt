import requests

class ExchangeRateGateway:
    BASE_URL = "https://api.exchangerate.host"
    ACCESS_KEY = "b529a01fb9adc36350583415088ef38a"

    def get_exchange_rate(self, from_currency: str, to_currency: str) -> float:
        url = f"{self.BASE_URL}/convert"
        params = {"from": from_currency, "to": to_currency}
        response = requests.get(url, params=params)

        if response.status_code != 200:
            raise Exception("Eroare la apelul API")

        data = response.json()
        print("DATA: ", data)
        return data["result"]

class CurrencyConverter:
    def __init__(self, gateway: ExchangeRateGateway):
        self.gateway = gateway

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        rate = self.gateway.get_exchange_rate(from_currency, to_currency)
        return amount * rate
