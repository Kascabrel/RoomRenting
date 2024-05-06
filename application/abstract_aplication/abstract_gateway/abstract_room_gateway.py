from abc import ABC

from application.abstract_aplication.abstract_gateway import AbstractModelGateway


class AbstractRoomGateway(ABC, AbstractModelGateway):
    def __init__(self):
        super().__init__()
