from abc import ABC, abstractmethod


class AbstractModelGateway(ABC):  # contains the abstract methods that will be implemented in the gateway layer

    @abstractmethod
    def get(self, model):
        raise NotImplementedError

    def get_all(self):
        raise NotImplementedError

    def create(self, model):
        raise NotImplementedError

    def delete(self, model):
        raise NotImplementedError
