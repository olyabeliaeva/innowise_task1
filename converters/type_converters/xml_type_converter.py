import logging
from typing import List

from dicttoxml import dicttoxml

from models.base_model import BaseModel


class XmlTypeConverter():

    def convert_models(self, models: List[BaseModel]):
        logging.info('Start saving xml file')
        with open(f'export_{type(models[0])}.xml', 'w') as f:
            data = str(dicttoxml(
                list(map(vars, models)),
                attr_type=False,
                custom_root='rooms'
            ))
            f.write(data)
