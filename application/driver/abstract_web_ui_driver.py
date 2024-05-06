from abc import ABC, abstractmethod

from application.driver import AbstractUIDriver, AbstractUIContext


class AbstractWebUIDriver(AbstractUIDriver, ABC):  # can be a FlaskDriver or DjangoDriver
    pass


class AbstractWebRequest(AbstractUIContext, ABC):
    """This class is a representation of a web request.
    It will be used those variables that are common for all web requests:
    - url_params for url parameters
    - form_data for form data
    - method for request method
    - session for session

    """

    def __init__(self, data, method: str, session: dict):
        self.data = data
        self.method = method
        self.session = session

    @abstractmethod
    def response_template(self):
        raise NotImplementedError

    @abstractmethod
    def response_redirect(self, url):
        raise NotImplementedError

    def response_json(self, data):
        raise NotImplementedError
