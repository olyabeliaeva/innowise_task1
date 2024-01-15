import logging
from typing import List

from converters.sql_converters.room_sql_converter import RoomSqlConverter
from converters.type_converters.type_converter import TypeConverter
from models.room import Room
from repositories.queries_repository import QueriesRepository
from repositories.room_repository import RoomRepository
from services.base_service import BaseService


class RoomService(BaseService):
    """
    A service class for handling operations related to rooms.

    This class inherits from BaseService.

    Attributes:
        room_sql_converter (RoomSqlConverter): An instance of the RoomSqlConverter class for converting between
                                               Room instances and SQL models.
        room_repository (RoomRepository): An instance of the RoomRepository class for executing room-related queries.
        type_converter (TypeConverter): An instance of the TypeConverter class for converting models.
        queries (QueriesRepository): An instance of the QueriesRepository class for executing queries.

    Methods:
        save_all(rooms: List[Room]) -> None:
            Save a list of rooms to the database.

        get_all() -> List[Room]:
            Retrieve all rooms from the database.

    Usage:
        # Example usage to save and retrieve rooms:
        service = RoomService()
        service.save_all(list_of_rooms)
        rooms = service.get_all()
    """

    def __init__(self):
        """
        Initialize a new instance of the RoomService class.
        Create instances of the RoomSqlConverter, RoomRepository, TypeConverter, and QueriesRepository classes.
        """
        super(RoomService, self).__init__()
        self.room_sql_converter = RoomSqlConverter()
        self.room_repository = RoomRepository()
        self.type_converter = TypeConverter()
        self.queries = QueriesRepository()

    def save_all(self, rooms: List[Room]) -> None:
        """
        Save a list of rooms to the database.

        Args:
            rooms (List[Room]): The list of Room instances to be saved.

        Returns:
            None
        """
        sql_models = self.room_sql_converter.convert_models_to_sql(rooms)
        self.room_repository.save_rooms(sql_models)
        logging.info('Rooms successfully saved to the DB')

    def get_all(self) -> List:
        """
        Retrieve all rooms from the database.

        Returns:
            List[Room]: The result of the query as a list of Room instances.
        """
        logging.info('Start getting data about rooms from DB')
        sql_models = self.room_repository.get_all()
        return self.room_sql_converter.convert_sql_to_models(sql_models)
