import logging
from typing import List

from constants.type_constants import ConvertType
from converters.sql_converters.room_sql_converter import RoomSqlConverter
from converters.type_converters.type_converter import TypeConverter
from models.room import Room
from repositories.room_repository import RoomRepository


class RoomService():

    def __init__(self):
        self.room_sql_converter = RoomSqlConverter()
        self.room_repository = RoomRepository()
        self.type_converter = TypeConverter()

    def save_all(self, rooms: List[Room]):
        sql_model = self.room_sql_converter.convert_models_to_sql(rooms)
        self.room_repository.save_rooms(sql_model)
        logging.info('Rooms successfully saved to the DB')

    def get_all(self) -> List[Room]:
        logging.info('Start getting data about rooms from DB')
        sql_models = self.room_repository.get_all()
        return self.room_sql_converter.convert_sql_to_models(sql_models)

    def save_to_file(self, models: List[Room], convert_type: ConvertType):
        self.type_converter.convert(models, convert_type)
        logging.info('File with rooms succsessfully saved')
