from typing import List

from constants.type_constants import ConvertType
from converters.type_converters.json_type_converter import JsonTypeConverter
from converters.type_converters.xml_type_converter import XmlTypeConverter
from models.base_model import BaseModel


class TypeConverter:
    """
    A class for converting models to different data formats based on the specified conversion type.

    Methods:
        convert(models: List[BaseModel], to_type: ConvertType) -> None:
            Convert a list of BaseModel instances to the specified data format.

    Attributes:
        convert_type_to_converters (dict): A mapping of ConvertType to corresponding type converters.

    Usage:
        # Example usage to convert a list of models to JSON format:
        converter = TypeConverter()
        converter.convert(list_of_models, ConvertType.JSON)
    """

    def __init__(self):
        """
        Initialize the TypeConverter with available type converters.
        """
        self.convert_type_to_converters = {
            ConvertType.JSON: JsonTypeConverter(),
            ConvertType.XML: XmlTypeConverter()
        }

    def convert(self, models: List[BaseModel], to_type: ConvertType) -> None:
        """
        Convert a list of BaseModel instances to the specified data format.

        Args:
            models (List[BaseModel]): The list of BaseModel instances to be converted.
            to_type (ConvertType): The target data format for conversion.

        Returns:
            None
        """
        return self.convert_type_to_converters.get(to_type).convert_models(models)
