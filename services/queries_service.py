from typing import List

from converters.sql_converters.query_model_sql_converter import \
    QueryModelSqlConverter
from repositories.queries_repository import QueriesRepository
from services.base_service import BaseService


class QueriesService(BaseService):
    """
    A service class for handling SQL queries related to rooms and students.

    This class inherits from BaseService.

    Attributes:
        queries_repository (QueriesRepository): An instance of the QueriesRepository class for executing queries.
        query_model_sql_converter (QueryModelSqlConverter): An instance of the QueryModelSqlConverter class for
                                                            converting between QueryModel instances and SQL models.

    Methods:
        get_list_of_rooms_with_quantity_students() -> List[QueryModel]:
            Retrieve a list of rooms with the quantity of students in each room.

        get_five_rooms_with_min_avg_age_of_students() -> List[QueryModel]:
            Retrieve five rooms with the minimum average age of students.

        get_five_rooms_with_max_difference_age_of_students() -> List[QueryModel]:
            Retrieve five rooms with the maximum difference in age among students.

        get_list_of_rooms_includes_students_with_different_sexes() -> List[QueryModel]:
            Retrieve a list of rooms that include students with different sexes.
    """

    def __init__(self):
        """
        Initialize a new instance of the QueriesService class.
        Create instances of the QueriesRepository and QueryModelSqlConverter classes.
        """
        super(QueriesService, self).__init__()
        self.queries_repository = QueriesRepository()
        self.query_model_sql_converter = QueryModelSqlConverter()

    def get_list_of_rooms_with_quantity_students(self) -> List:
        """
        Retrieve a list of rooms with the quantity of students in each room.

        Returns:
            List: The result of the query as a list of QueryModel instances.
        """
        sql_query_models = self.queries_repository.get_list_of_rooms_with_quantity_students()
        return self.query_model_sql_converter.convert_sql_to_models(sql_query_models)

    def get_five_rooms_with_min_avg_age_of_students(self) -> List:
        """
        Retrieve five rooms with the minimum average age of students.

        Returns:
            List[QueryModel]: The result of the query as a list of QueryModel instances.
        """
        sql_query_models = self.queries_repository.get_five_rooms_with_min_avg_age_of_students()
        return self.query_model_sql_converter.convert_sql_to_models(sql_query_models)

    def get_five_rooms_with_max_difference_age_of_students(self) -> List:
        """
        Retrieve five rooms with the maximum difference in age among students.

        Returns:
            List: The result of the query as a list of QueryModel instances.
        """
        sql_query_models = self.queries_repository.get_five_rooms_with_max_difference_age_of_students()
        return self.query_model_sql_converter.convert_sql_to_models(sql_query_models)

    def get_list_of_rooms_includes_students_with_different_sexes(self) -> List:
        """
        Retrieve a list of rooms that include students with different sexes.

        Returns:
            List: The result of the query as a list of QueryModel instances.
        """
        sql_query_models = self.queries_repository.get_list_of_rooms_includes_students_with_different_sexes()
        return self.query_model_sql_converter.convert_sql_to_models(sql_query_models)
