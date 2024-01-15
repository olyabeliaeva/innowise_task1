import json
import logging
from abc import ABC, abstractmethod


class JsonReader(ABC):

    def read_json(self, file_path: str):
        logging.info(f'Reading json file named {file_path}')
        with open(file_path, 'r') as file:
            return json.load(file, object_hook=self._get_model_hook())

    @abstractmethod
    def _get_model_hook(self):
        pass
