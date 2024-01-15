from json_reader.json_reader import JsonReader
from models.student import Student


class StudentsJsonReader(JsonReader):
    """
    A JSON reader specifically designed for reading Student objects from JSON files.

    This class inherits from JsonReader.

    Methods:
        _get_model_hook() -> callable:
            Get a custom hook function for decoding JSON objects into Student instances.
    """

    def _get_model_hook(self) -> callable:
        """
        Get a custom hook function for decoding JSON objects into Student instances.

        Returns:
            callable: The custom hook function.
        """
        return lambda values: Student(**values)
