from abc import ABC, abstractmethod

from application.driver import AbstractUIContext
from domain.entities.room import Room


class AbstractRoomController(ABC):
    @abstractmethod
    def get_room(self, room_id: int) -> Room:
        pass

    @abstractmethod
    def get_rooms(self) -> list[Room]:
        pass

    @abstractmethod
    def create_room(self, context: AbstractUIContext):
        raise NotImplementedError

    @abstractmethod
    def update_room(self, context: AbstractUIContext):
        raise NotImplementedError

    @abstractmethod
    def delete_room(self, context: AbstractUIContext):
        raise NotImplementedError

    @abstractmethod
    def show_rooms(self, context: AbstractUIContext):
        raise NotImplementedError
