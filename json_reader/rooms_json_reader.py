from json_reader.json_reader import JsonReader
from models.room import Room


class RoomsJsonReader(JsonReader):
    """
    A JSON reader specifically designed for reading Room objects from JSON files.

    This class inherits from JsonReader.

    Methods:
        _get_model_hook() -> callable:
            Get a custom hook function for decoding JSON objects into Room instances.
    """

    def _get_model_hook(self) -> callable:
        """
        Get a custom hook function for decoding JSON objects into Room instances.

        Returns:
            callable: The custom hook function.
        """
        return lambda values: Room(**values)
