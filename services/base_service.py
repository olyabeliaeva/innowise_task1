import logging
from typing import List

from constants.type_constants import ConvertType
from converters.type_converters.type_converter import TypeConverter
from models.base_model import BaseModel


class BaseService:

    def __init__(self):
        self.type_converter = TypeConverter()

    def save_to_file(self, models: List[BaseModel], convert_type: ConvertType):
        self.type_converter.convert(models, convert_type)
        logging.info('File with rooms succsessfully saved')
