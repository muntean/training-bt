from ..base.mediator_base import MediatorBase
from ..colleague.user import User

class MediatorApp(MediatorBase):
    def __init__(self):
        self.users = []

    def register(self, user: User):
        self.users.append(user)
        user.mediator = self

    def send_message(self, message: str, sender: User):
        for user in self.users:
            if user.id != sender.id:
                user.receive(message)

class Adder:
    def compute(self, *args):
        return sum(args)
class Multiplier:
    def compute(self, *args):
        product = 1
        if args:
            for number in args:
                product *= number
        return product

class Calculator:
    def execute(self, operation, *args):
        if operation == 'add':
            return Adder().compute(*args)
        elif operation == 'multiply':
            return Multiplier().compute(*args)
        else:
            raise ValueError(f"Operația '{operation}' nu e suportată")


