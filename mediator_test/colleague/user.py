from ..base.mediator_base import MediatorBase
from ..base.user_base import UserBase

class User(UserBase):
    _next_id = 1

    def __init__(self, name: str):
        self.id = type(self)._next_id
        self.name = name
        self.mediator: MediatorBase | None = None
        type(self)._next_id += 1

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}')"

    def send(self, message: str):
        print(f"{self.name} send: {message}")
        self.mediator.send_message(message, self)

    def receive(self, message: str):
        print(f"{self.name} receive: {message}")