import logging
from typing import List

from constants.type_constants import ConvertType
from converters.type_converters.type_converter import TypeConverter
from models.base_model import BaseModel


class BaseService:
    """
    A base service class for handling common operations related to models.

    Attributes:
        type_converter (TypeConverter): An instance of the TypeConverter class for converting models.

    Methods:
        save_to_file(models: List[BaseModel], convert_type: ConvertType) -> None:
            Save models to a file in the specified data format.

    Usage:
        # Example usage to save a list of models to a file in JSON format:
        service = BaseService()
        service.save_to_file(list_of_models, ConvertType.JSON)
    """

    def __init__(self):
        """
        Initialize a new instance of the BaseService class.
        Create an instance of the TypeConverter class for converting models.
        """
        self.type_converter = TypeConverter()

    def save_to_file(self, models: List[BaseModel], convert_type: ConvertType) -> None:
        """
        Save models to a file in the specified data format.

        Args:
            models (List[BaseModel]): The list of BaseModel instances to be saved.
            convert_type (ConvertType): The target data format for saving.

        Returns:
            None
        """
        self.type_converter.convert(models, convert_type)
        logging.info('File with models successfully saved')
