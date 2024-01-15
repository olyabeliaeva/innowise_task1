from converters.sql_converters.sql_converter import ModelSqlConverter
from models.room import Room


class RoomSqlConverter(ModelSqlConverter):
    """
    A SQL converter for converting between Room instances and their corresponding SQL representation.

    This class inherits from ModelSqlConverter.

    Methods:
        _convert_model(model: Room) -> tuple:
            Convert a Room instance to its SQL representation.

        _convert_sql_to_model(sql_model: tuple) -> Room:
            Convert a SQL representation (tuple) to a Room instance.
    """

    def _convert_model(self, model: Room) -> tuple:
        """
        Convert a Room instance to its SQL representation.

        Args:
            model (Room): The Room instance to be converted.

        Returns:
            tuple: The SQL representation of the Room instance.
        """
        return (model.id, model.name)

    def _convert_sql_to_model(self, sql_model: tuple) -> Room:
        """
        Convert a SQL representation (tuple) to a Room instance.

        Args:
            sql_model (tuple): The SQL representation of a Room instance.

        Returns:
            Room: The Room instance created from the SQL representation.
        """
        return Room(sql_model[0], sql_model[1])
