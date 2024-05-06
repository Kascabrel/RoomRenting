from application.abstract_aplication.abstract_gateway.abstract_room_gateway import AbstractRoomGateway
from application.abstract_aplication.abstract_presenter.abstract_room_presenter import AbstractRoomPresenter
from application.driver import AbstractUIContext
from domain.entities.room import Room


class RoomUseCase:
    def __init__(self, room_presenter: AbstractRoomPresenter, room_gateway: AbstractRoomGateway):
        self.room_presenter = room_presenter
        self.room_gateway = room_gateway

    def create_room(self,
                    context: AbstractUIContext,
                    room_name: str,
                    room_avability: bool,
                    roo_description: str,
                    room_location_price: int):
        room = self.room_gateway.create(Room(None, room_name, room_avability, roo_description, room_location_price))
        self.room_presenter.show_message(context, f"Room {room.name} created")
        self.room_presenter.show_room(context, room)

    def delete_room(self, context: AbstractUIContext, room_id: int):
        room = self.room_gateway.get(room_id)
        self.room_gateway.delete(room)
        self.room_presenter.show_message(context, f"Room {room.name} deleted")
        self.show_all_rooms(context)

    def how_room(self, context: AbstractUIContext, room_id: int):
        room = self.room_gateway.get(room_id)
        self.room_presenter.show_room(context, room)

    def show_all_rooms(self, context: AbstractUIContext):
        rooms = self.room_gateway.get_all()
        self.room_presenter.show_rooms(context, rooms)
