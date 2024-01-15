import json
import logging
from typing import List

from models.base_model import BaseModel


class JsonTypeConverter():

    def convert_models(self, models: List[BaseModel]):
        logging.info('Start saving json file')
        with open(f'export_{type(models[0])}.json', 'w') as f:
            json.dump(list(map(lambda model: model.__dict__, models)), f, default=str)
