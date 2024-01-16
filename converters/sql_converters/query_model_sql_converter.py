from converters.sql_converters.sql_converter import ModelSqlConverter
from models.query_model import QueryModel


class QueryModelSqlConverter(ModelSqlConverter):
    """
    A SQL converter for converting between QueryModel instances and their corresponding SQL representation.

    This class inherits from ModelSqlConverter.

    Methods:
        _convert_model(model: QueryModel) -> tuple:
            Convert a QueryModel instance to its SQL representation.

        _convert_sql_to_model(sql_model: tuple) -> QueryModel:
            Convert a SQL representation (tuple) to a QueryModel instance.
    """

    def _convert_model(self, model: QueryModel) -> tuple:
        """
        Convert a QueryModel instance to its SQL representation.

        Args:
            model (QueryModel): The QueryModel instance to be converted.

        Returns:
            tuple: The SQL representation of the QueryModel instance.
        """
        return (model.id, model.name, model.info)

    def _convert_sql_to_model(self, sql_model: tuple) -> QueryModel:
        """
        Convert a SQL representation (tuple) to a QueryModel instance.

        Args:
            sql_model (tuple): The SQL representation of a QueryModel instance.

        Returns:
            QueryModel: The QueryModel instance created from the SQL representation.
        """
        return QueryModel(sql_model[0], sql_model[1], sql_model[2])
