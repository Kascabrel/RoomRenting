from abc import abstractmethod, ABC

from application.driver import AbstractUIContext


class AbstractPresenter(ABC):
    @abstractmethod
    def show_message(self,context: AbstractUIContext,  message: str):  # use to show message independent of view. will be  implement in ui layer
        raise