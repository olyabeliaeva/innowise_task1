import unittest

from converters.sql_converters.student_sql_converter import StudentSqlConverter
from models.student import Student


class TestStudentSqlConverter(unittest.TestCase):
    """
    Unit tests for the StudentSqlConverter class.

    This class inherits from unittest.TestCase and contains two test methods:
    - test__convert_model: Tests the _convert_model method of StudentSqlConverter.
    - test__convert_sql_to_model: Tests the _convert_sql_to_model method of StudentSqlConverter.
    """

    def test__convert_model(self):
        """
        Test the _convert_model method of StudentSqlConverter.

        Creates a test Student instance, converts it to a SQL model, and compares the result with the expected outcome.
        """
        test_student = Student(
            id=1,
            name='John Doe',
            birthday='1990-01-01',
            room='101',
            sex='M'
        )
        student_sql_converter = StudentSqlConverter()

        self.assertEqual(
            student_sql_converter._convert_model(test_student),
            ('1990-01-01', 1, 'John Doe', '101', 'M')
        )

    def test__convert_sql_to_model(self):
        """
        Test the _convert_sql_to_model method of StudentSqlConverter.

        Creates a test SQL model, converts it to a Student instance, and compares the result with the expected outcome.
        """
        test_sql_model = ('1990-01-01', 100, 'John Doe', 101, 'M')
        student_sql_converter = StudentSqlConverter()
        student = student_sql_converter._convert_sql_to_model(test_sql_model)
        self.assertEqual(student.id, 100)
        self.assertEqual(student.birthday, '1990-01-01')
        self.assertEqual(student.name, 'John Doe')
        self.assertEqual(student.room, 101)
        self.assertEqual(student.sex, 'M')


if __name__ == '__main__':
    unittest.main()
