import logging
from typing import List

from converters.sql_converters.room_sql_converter import RoomSqlConverter
from converters.type_converters.type_converter import TypeConverter
from models.room import Room
from repositories.queries_repository import QueriesRepository
from repositories.room_repository import RoomRepository
from services.base_service import BaseService


class RoomService(BaseService):

    def __init__(self):
        super(RoomService, self).__init__()
        self.room_sql_converter = RoomSqlConverter()
        self.room_repository = RoomRepository()
        self.type_converter = TypeConverter()
        self.queries = QueriesRepository()

    def save_all(self, rooms: List[Room]):
        sql_model = self.room_sql_converter.convert_models_to_sql(rooms)
        self.room_repository.save_rooms(sql_model)
        logging.info('Rooms successfully saved to the DB')

    def get_all(self) -> List[Room]:
        logging.info('Start getting data about rooms from DB')
        sql_models = self.room_repository.get_all()
        return self.room_sql_converter.convert_sql_to_models(sql_models)
