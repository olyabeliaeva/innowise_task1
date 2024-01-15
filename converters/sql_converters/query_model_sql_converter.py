from converters.sql_converters.sql_converter import ModelSqlConverter
from models.query_model import QueryModel


class QueryModelSqlConverter(ModelSqlConverter):

    def _convert_model(self, model: QueryModel) -> tuple:
        return (model.id, model.name, model.info)

    def _convert_sql_to_model(self, sql_model: tuple) -> QueryModel:
        return QueryModel(sql_model[0], sql_model[1], sql_model[2])
