import unittest
from unittest import TestCase

from converters.sql_converters.query_model_sql_converter import QueryModelSqlConverter
from models.query_model import QueryModel


class TestQueryModelSqlConverter(TestCase):
    def test__convert_model(self):
        test_query_model = QueryModel(
            id=1,
            name='Room #1',
            info=123

        )

        query_converter = QueryModelSqlConverter()
        result = query_converter._convert_model(test_query_model)
        expected_result = (1, 'Room #1', 123)
        self.assertEqual(result, expected_result)

    def test__convert_sql_to_model(self):
        test_sql_query_model = (69, 'Room #69', 123)
        query_sql_converter = QueryModelSqlConverter()
        query = query_sql_converter._convert_sql_to_model(test_sql_query_model)

        self.assertEqual(query.id, 69)
        self.assertEqual(query.name, 'Room #69')
        self.assertEqual(query.info, 123)


if __name__ == '__main__':
    unittest.main()
