import requests

class NumberVerifyGateway:
    VERSION = ""
    BASE_URL = "https://apilayer.net/api"
    ACCESS_KEY = "715c861ee06aee04a67395123edce432"

    def __init__(self, environment: dict=None):
        self.env = environment

    def _get_base_url(self):
        """Return base url"""
        if not self.env:
            return self.BASE_URL
        return self.env['base_url']

    def _get_access_key(self):
        """Return access key"""
        if not self.env:
            return self.ACCESS_KEY
        return self.env['access_key']

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

    def validate(self, number: str, country_code: str=None, callback: str=None, response_format: int=None):
        """Validate phone number"""
        params = {
            "number": number,
        }
        if country_code and len(country_code) == 2:
            params['country_code'] = country_code
        if callback:
            params['callback'] = callback
        if response_format:
            params['format'] = str(response_format)
        return self._get("validate", params=params)

    def countries(self):
        """Retrieve all country codes"""
        return self._get("validate")


if __name__ == "__main__":
    gateway = NumberVerifyGateway()
    varification = gateway.validate(number='0745430371', country_code="RO", response_format=1)
    print(varification)

# {'valid': True, 'number': '40745631242', 'local_format': '0745631242', 'international_format': '+40745631242', 'country_prefix': '+40', 'country_code': 'RO', 'country_name': 'Romania', 'location': '', 'carrier': 'Orange Romania SA', 'line_type': 'mobile'} apel cu number='0040745631242'
# {'valid': True, 'number': '40743391876', 'local_format': '0743391876', 'international_format': '+40743391876', 'country_prefix': '+40', 'country_code': 'RO', 'country_name': 'Romania', 'location': '', 'carrier': 'Orange Romania SA', 'line_type': 'mobile'} apel cu response_format=1, number='+40743391876'
# {'valid': True, 'number': '400745430371', 'local_format': '0745430371', 'international_format': '+40745430371', 'country_prefix': '+40', 'country_code': 'RO', 'country_name': 'Romania', 'location': '', 'carrier': 'Orange Romania SA', 'line_type': 'mobile'} apel cu country_code="RO"