from abc import ABC, abstractmethod
from typing import List

from models.base_model import BaseModel


class ModelSqlConverter(ABC):

    def convert_models_to_sql(self, models: List[BaseModel]):
        converted_models = []
        for model in models:
            converted_models.append(self._convert_model(model))
        return converted_models

    @abstractmethod
    def _convert_model(self, model: BaseModel):
        pass

    def convert_sql_to_models(self, sql_models):
        converted_models = []
        for sql_model in sql_models:
            converted_models.append(self._convert_sql_to_model(sql_model))
        return converted_models

    @abstractmethod
    def _convert_sql_to_model(self, sql_model):
        pass
