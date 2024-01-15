from converters.sql_converters.sql_converter import ModelSqlConverter
from models.room import Room


class RoomSqlConverter(ModelSqlConverter):

    def _convert_model(self, model: Room) -> tuple:
        return (model.id, model.name)

    def _convert_sql_to_model(self, sql_model: tuple) -> Room:
        return Room(sql_model[0], sql_model[1])
