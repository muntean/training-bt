import unittest
from unittest.mock import MagicMock

# from ..api_gateway.gateway import UserApiGateway, DisplayUser
from ..api_gateway.gateway_test_disp import UserApiGateway, DisplayUser

class TestCases(unittest.TestCase):
    def test_user_api_gateway(self):
        mock_gateway = MagicMock(spec=UserApiGateway)
        mock_gateway.get_user.return_value = {'name': 'Test User', 'email': 'test@example.com'}

        user_info = DisplayUser(mock_gateway)
        user = user_info.get_user_info(1)

        self.assertEqual(user['name'], 'Test User')
        self.assertEqual(user['email'], 'test@example.com')

    def test_users_api_gateway(self):
        mock_gateway = MagicMock(spec=UserApiGateway)
        mock_gateway.get_user.return_value = [{'name': 'Test User', 'email': 'test@example.com'}, {'name': 'Test User2', 'email': 'test2@example.com'}]
        user_info = DisplayUser(mock_gateway)
        users = user_info.get_users()
        self.assertEqual(len(users), 2)

    def my_side_effect(self):
        raise Exception("Test")

if __name__ == '__main__':
    unittest.main()