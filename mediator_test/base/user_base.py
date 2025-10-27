import abc

class UserBase(abc.ABC):
    @abc.abstractmethod
    def send(self, message: str):
        pass

    @abc.abstractmethod
    def receive(self, message: str):
        pass