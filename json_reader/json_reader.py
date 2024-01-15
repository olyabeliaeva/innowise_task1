import json
import logging
from abc import ABC, abstractmethod
from typing import Any


class JsonReader(ABC):
    """
    An abstract base class for reading JSON files and converting them into Python objects.

    Methods:
        read_json(file_path: str) -> Any:
            Read a JSON file and return the corresponding Python object.

    Abstract Methods:
        _get_model_hook() -> callable:
            Abstract method to get a custom hook function for decoding JSON objects.

    Usage:
        # Example usage to read a JSON file and get Python objects:
        reader = YourJsonReaderClass()
        data = reader.read_json('path/to/your/file.json')
    """

    def read_json(self, file_path: str) -> Any:
        """
        Read a JSON file and return the corresponding Python object.

        Args:
            file_path (str): The path to the JSON file to be read.

        Returns:
            Any: The Python object decoded from the JSON file.
        """
        logging.info(f'Reading json file named {file_path}')
        with open(file_path, 'r') as file:
            return json.load(file, object_hook=self._get_model_hook())

    @abstractmethod
    def _get_model_hook(self) -> callable:
        """
        Abstract method to get a custom hook function for decoding JSON objects.

        Returns:
            callable: The custom hook function.
        """
        pass
