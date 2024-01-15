import unittest
from unittest.mock import patch

from constants.type_constants import ConvertType
from models.query_model import QueryModel
from services.queries_service import QueriesService


class QueriesServiceTest(unittest.TestCase):
    """
    Unit tests for the QueriesService class.

    This class inherits from unittest.TestCase and contains tests for various methods of the QueriesService class.
    """

    def setUp(self):
        """
        Set up the necessary instances for each test method.
        """
        self.queries_service = QueriesService()

    @patch('repositories.queries_repository.QueriesRepository')
    @patch('converters.sql_converters.query_model_sql_converter.QueryModelSqlConverter')
    def test_get_list_of_rooms_with_quantity_students(self, mock_query_model_sql_converter,
                                                      mock_queries_repository):
        """
        Test the get_list_of_rooms_with_quantity_students method of QueriesService.

        Mocks the dependencies and checks if the appropriate methods are called.
        """
        mock_converter_instance = mock_query_model_sql_converter.return_value
        mock_repository_instance = mock_queries_repository.return_value
        self.queries_service.query_model_sql_converter = mock_converter_instance
        self.queries_service.queries_repository = mock_repository_instance
        result = self.queries_service.get_list_of_rooms_with_quantity_students()
        mock_repository_instance.get_list_of_rooms_with_quantity_students.assert_called_once()
        mock_converter_instance.convert_sql_to_models.assert_called_once()
        self.assertEqual(result, mock_converter_instance.convert_sql_to_models.return_value)

    @patch('repositories.queries_repository.QueriesRepository')
    @patch('converters.sql_converters.query_model_sql_converter.QueryModelSqlConverter')
    def test_get_five_rooms_with_min_avg_age_of_students(self, mock_query_model_sql_converter,
                                                         mock_queries_repository):
        """
        Test the get_five_rooms_with_min_avg_age_of_students method of QueriesService.

        Mocks the dependencies and checks if the appropriate methods are called.
        """
        mock_converter_instance = mock_query_model_sql_converter.return_value
        mock_repository_instance = mock_queries_repository.return_value
        self.queries_service.query_model_sql_converter = mock_converter_instance
        self.queries_service.queries_repository = mock_repository_instance
        result = self.queries_service.get_five_rooms_with_min_avg_age_of_students()
        mock_repository_instance.get_five_rooms_with_min_avg_age_of_students.assert_called_once()
        mock_converter_instance.convert_sql_to_models.assert_called_once()
        self.assertEqual(result, mock_converter_instance.convert_sql_to_models.return_value)

    @patch('repositories.queries_repository.QueriesRepository')
    @patch('converters.sql_converters.query_model_sql_converter.QueryModelSqlConverter')
    def test_get_five_rooms_with_max_difference_age_of_students(self, mock_query_model_sql_converter,
                                                                mock_queries_repository):
        """
        Test the get_five_rooms_with_max_difference_age_of_students method of QueriesService.

        Mocks the dependencies and checks if the appropriate methods are called.
        """
        mock_converter_instance = mock_query_model_sql_converter.return_value
        mock_repository_instance = mock_queries_repository.return_value
        self.queries_service.query_model_sql_converter = mock_converter_instance
        self.queries_service.queries_repository = mock_repository_instance
        result = self.queries_service.get_five_rooms_with_max_difference_age_of_students()
        mock_repository_instance.get_five_rooms_with_max_difference_age_of_students.assert_called_once()
        mock_converter_instance.convert_sql_to_models.assert_called_once()
        self.assertEqual(result, mock_converter_instance.convert_sql_to_models.return_value)

    @patch('repositories.queries_repository.QueriesRepository')
    @patch('converters.sql_converters.query_model_sql_converter.QueryModelSqlConverter')
    def test_get_list_of_rooms_includes_students_with_different_sexes(self, mock_query_model_sql_converter,
                                                                      mock_queries_repository):
        """
        Test the get_list_of_rooms_includes_students_with_different_sexes method of QueriesService.

        Mocks the dependencies and checks if the appropriate methods are called.
        """
        mock_converter_instance = mock_query_model_sql_converter.return_value
        mock_repository_instance = mock_queries_repository.return_value
        self.queries_service.query_model_sql_converter = mock_converter_instance
        self.queries_service.queries_repository = mock_repository_instance
        result = self.queries_service.get_list_of_rooms_includes_students_with_different_sexes()
        mock_repository_instance.get_list_of_rooms_includes_students_with_different_sexes.assert_called_once()
        mock_converter_instance.convert_sql_to_models.assert_called_once()
        self.assertEqual(result, mock_converter_instance.convert_sql_to_models.return_value)

    @patch('converters.type_converters.type_converter.TypeConverter')
    def test_save_to_file(self, mock_type_converter):
        """
        Test the save_to_file method of QueriesService.

        Mocks the dependencies and checks if the appropriate methods are called.
        """
        query_models = [
            QueryModel(id=1, name='Room#1', info=1),
            QueryModel(id=2, name='Room# 2', info=2),
        ]
        convert_type = ConvertType.JSON
        mock_converter_instance = mock_type_converter.return_value
        self.queries_service.type_converter = mock_converter_instance
        self.queries_service.save_to_file(query_models, convert_type)
        mock_converter_instance.convert.assert_called_once_with(query_models, convert_type)


if __name__ == '__main__':
    unittest.main()
