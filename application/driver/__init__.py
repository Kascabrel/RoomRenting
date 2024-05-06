from abc import abstractmethod, ABC


class AbstractUIContext:  # in our case it will be a Webrequest
    pass


class AbstractUIDriver(ABC):  # can be a FlaskDriver or DjangoDriver for web context
    @abstractmethod
    def sow_message(self, message: str):
        raise NotImplementedError
