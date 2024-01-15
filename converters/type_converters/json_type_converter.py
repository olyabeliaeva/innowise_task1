import json
import logging
from typing import List

from models.base_model import BaseModel


class JsonTypeConverter:
    """
    A class for converting models to JSON format and saving them to a file.

    Methods:
        convert_models(models: List[BaseModel]) -> None:
            Convert a list of BaseModel instances to JSON format and save them to a file.

    Usage:
        # Example usage to convert and save a list of models to a JSON file:
        converter = JsonTypeConverter()
        converter.convert_models(list_of_models)
    """

    def convert_models(self, models: List[BaseModel]) -> None:
        """
        Convert a list of BaseModel instances to JSON format and save them to a file.

        Args:
            models (List[BaseModel]): The list of BaseModel instances to be converted and saved.

        Returns:
            None
        """
        logging.info('Start saving json file')
        with open(f'export_{type(models[0])}.json', 'w') as f:
            json.dump(list(map(lambda model: model.__dict__, models)), f, default=str)
