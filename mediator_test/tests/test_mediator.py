import unittest
from ..colleague.user import User
from ..mediator_app.mediator_app import MediatorApp, Calculator
# from unittest.mock import MagicMock

class TestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chat = MediatorApp()
        cls.user1 = User("Ana")
        cls.user2 = User("Mihai")
        cls.user3 = User("Maria")

        cls.chat.register(cls.user1)
        cls.chat.register(cls.user2)
        cls.chat.register(cls.user3)

    def test_send_message(self):
        self.user1.send("Salut tuturor!")
        self.user2.send("Salut, Ana!")
        self.user3.send("Salut, Ana!")

    def test_calculator_add(self):
        calculator = Calculator()
        add = calculator.execute('add', 1,2,3,4)
        expected_result = 10
        self.assertEqual(expected_result, add)

    def test_calculator_multiply(self):
        calculator = Calculator()
        product = calculator.execute('multiply', 1,2,3,4)
        expected_result = 24
        self.assertEqual(expected_result, product)


if __name__ == '__main__':
    unittest.main()





