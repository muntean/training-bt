from abc import ABC, abstractmethod

class MediatorBase(ABC):

    @abstractmethod
    def send_message(self, message: str, sender) -> None:
        pass