import requests

class ExchangeGateway:
    BASE_URL = "https://api.currencylayer.com"
    ACCESS_KEY = "31d68f0e34fb2f94ce162e2ba86c5c06"

    def __init__(self, test_mode=False):
        self.test_mode = test_mode

    def _get_base_url(self):
        """Return base url"""
        if self.test_mode:
            return "https://api.exchangerate.host"
        return self.BASE_URL

    def _get_access_key(self):
        """Return access key"""
        if self.test_mode:
            return "b529a01fb9adc36350583415088ef38a"
        return self.ACCESS_KEY

    def _get(self, endpoint, params=None):
        """
        Make request call on endpoint with parameters
        :return response
        """
        if params is None:
            params = {}

        params["access_key"] = self._get_access_key()

        url = f"{self._get_base_url()}/{endpoint}"
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def live(self):
        """Return most recent exchange rates"""
        return self._get("live")

    def historical(self, date):
        """Return exchange rates for a specific date"""
        return self._get("historical", params={"date": date})

    def convert(self, from_currency, to_currency, amount):
        """Convert a value of a currency to other currency"""
        return self._get("convert", params={
            "from": from_currency,
            "to": to_currency,
            "amount": amount
        })

    def timeframe(self, start_date, end_date):
        """Return exchange rates between start and end date"""
        return self._get("timeframe", params={
            "start_date": start_date,
            "end_date": end_date
        })

    def change(self, currencies):
        """Return currency's change for currencies"""
        return self._get("change", params={
            "currencies": ",".join(currencies)
        })


if __name__ == "__main__":
    gateway = ExchangeGateway(test_mode=True)

    print("\n🔹 Convert 10 EUR to GBP:")
    print(gateway.convert("EUR", "GBP", 10))
