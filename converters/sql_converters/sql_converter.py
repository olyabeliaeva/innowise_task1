from abc import ABC, abstractmethod
from typing import List

from models.base_model import BaseModel


class ModelSqlConverter(ABC):
    """
    An abstract base class for defining the interface of SQL converters for model objects.

    Inherited classes must implement the abstract methods '_convert_model' and '_convert_sql_to_model'.

    Methods:
        convert_models_to_sql(models: List[BaseModel]) -> List:
            Convert a list of model instances to their SQL representations.

        convert_sql_to_models(sql_models: List) -> List[BaseModel]:
            Convert a list of SQL representations to their corresponding model instances.

    Abstract Methods:
        _convert_model(model: BaseModel) -> Any:
            Convert a model instance to its SQL representation.

        _convert_sql_to_model(sql_model: Any) -> BaseModel:
            Convert a SQL representation to its corresponding model instance.
    """

    def convert_models_to_sql(self, models: List[BaseModel]) -> List[tuple]:
        """
        Convert a list of model instances to their SQL representations.

        Args:
            models (List[BaseModel]): The list of model instances to be converted.

        Returns:
            List: The list of SQL representations of the model instances.
        """
        converted_models = []
        for model in models:
            converted_models.append(self._convert_model(model))
        return converted_models

    @abstractmethod
    def _convert_model(self, model: BaseModel) -> tuple:
        """
        Convert a model instance to its SQL representation.

        Args:
            model (BaseModel): The model instance to be converted.

        Returns:
            tuple: The SQL representation of the model instance.
        """
        pass

    def convert_sql_to_models(self, sql_models: List[tuple]) -> List[BaseModel]:
        """
        Convert a list of SQL representations to their corresponding model instances.

        Args:
            sql_models (List): The list of SQL representations to be converted.

        Returns:
            List[BaseModel]: The list of model instances created from the SQL representations.
        """
        converted_models = []
        for sql_model in sql_models:
            converted_models.append(self._convert_sql_to_model(sql_model))
        return converted_models

    @abstractmethod
    def _convert_sql_to_model(self, sql_model: tuple) -> BaseModel:
        """
        Convert a SQL representation to its corresponding model instance.

        Args:
            sql_model (Any): The SQL representation to be converted.

        Returns:
            BaseModel: The model instance created from the SQL representation.
        """
        pass
