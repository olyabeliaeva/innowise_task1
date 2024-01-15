import logging
from typing import List

from dicttoxml import dicttoxml

from models.base_model import BaseModel


class XmlTypeConverter:
    """
    A class for converting models to XML format and saving them to a file.

    Methods:
        convert_models(models: List[BaseModel]) -> None:
            Convert a list of BaseModel instances to XML format and save them to a file.

    Usage:
        # Example usage to convert and save a list of models to an XML file:
        converter = XmlTypeConverter()
        converter.convert_models(list_of_models)
    """

    def convert_models(self, models: List[BaseModel]) -> None:
        """
        Convert a list of BaseModel instances to XML format and save them to a file.

        Args:
            models (List[BaseModel]): The list of BaseModel instances to be converted and saved.

        Returns:
            None
        """
        logging.info('Start saving xml file')
        with open(f'export_{type(models[0])}.xml', 'w') as f:
            data = str(dicttoxml(
                list(map(vars, models)),
                attr_type=False,
                custom_root='rooms'
            ))
            f.write(data)
