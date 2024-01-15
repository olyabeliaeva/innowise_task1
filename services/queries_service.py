from converters.sql_converters.query_model_sql_converter import QueryModelSqlConverter
from repositories.queries_repository import QueriesRepository
from services.base_service import BaseService


class QueriesService(BaseService):
    def __init__(self):
        super(QueriesService, self).__init__()
        self.queries_repository = QueriesRepository()
        self.query_model_sql_converter = QueryModelSqlConverter()

    def get_list_of_rooms_with_quantity_students(self):
        sql_query_models = self.queries_repository.get_list_of_rooms_with_quantity_students()
        return self.query_model_sql_converter.convert_sql_to_models(sql_query_models)

    def get_five_rooms_with_min_avg_age_of_students(self):
        sql_query_models = self.queries_repository.get_five_rooms_with_min_avg_age_of_students()
        return self.query_model_sql_converter.convert_sql_to_models(sql_query_models)

    def get_five_rooms_with_max_difference_age_of_students(self):
        sql_query_models = self.queries_repository.get_five_rooms_with_max_difference_age_of_students()
        return self.query_model_sql_converter.convert_sql_to_models(sql_query_models)

    def get_list_of_rooms_includes_students_with_different_sexes(self):
        sql_query_models = self.queries_repository.get_list_of_rooms_includes_students_with_different_sexes()
        return self.query_model_sql_converter.convert_sql_to_models(sql_query_models)
