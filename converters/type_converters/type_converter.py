from typing import List

from constants.type_constants import ConvertType
from converters.type_converters.json_type_converter import JsonTypeConverter
from converters.type_converters.xml_type_converter import XmlTypeConverter
from models.base_model import BaseModel


class TypeConverter():

    def __init__(self):
        self.convert_type_to_converters = {
            ConvertType.JSON: JsonTypeConverter(),
            ConvertType.XML: XmlTypeConverter()
        }

    def convert(self, models: List[BaseModel], to_type: ConvertType):
        return self.convert_type_to_converters.get(to_type).convert_models(models)
