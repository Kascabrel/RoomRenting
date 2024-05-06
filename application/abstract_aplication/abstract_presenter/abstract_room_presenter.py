from abc import ABC, abstractmethod

from application.abstract_aplication.abstract_presenter.__init_ import AbstractPresenter
from application.driver import AbstractUIContext
from domain.entities.room import Room


class AbstractRoomPresenter(ABC, AbstractPresenter):

    @abstractmethod
    def show_room(self, context: AbstractUIContext, room: Room):
        raise NotImplementedError()

    @abstractmethod
    def show_rooms(self, context: AbstractUIContext, rooms: list[Room]):
        raise NotImplementedError()

