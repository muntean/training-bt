import unittest
from unittest.mock import MagicMock

from netifaces import gateways

from ..api_gateway.exchange_converter import ExchangeRateGateway

class TestCurrencyConverter(unittest.TestCase):
    # def test_convert_with_mock_gateway(self):
    #     mock_gateway = MagicMock(spec=ExchangeRateGateway)
    #     mock_gateway.get_exchange_rate.return_value = 4.5
    #
    #     # converter = CurrencyConverter(mock_gateway)
    #
    #     # result = converter.convert(100, "EUR", "RON")
    #
    #     self.assertEqual(result, 450.0)
    #     mock_gateway.get_exchange_rate.assert_called_once_with("EUR", "RON")

    def test_apel_efectiv(self):
        gateway = ExchangeRateGateway()
        # converter = CurrencyConverter(gateway)
        print(f"Convert: 10 EUR = {gateway.convert(10, 'EUR', 'GBP')} GBP")

if __name__ == "__main__":
    unittest.main()