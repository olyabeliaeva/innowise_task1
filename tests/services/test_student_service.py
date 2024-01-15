import unittest
from unittest.mock import patch

from constants.type_constants import ConvertType
from models.student import Student
from services.student_service import StudentService


class StudentServiceTest(unittest.TestCase):
    """
    Unit tests for the StudentService class.

    This class inherits from unittest.TestCase and contains tests for various methods of the StudentService class.
    """

    def setUp(self):
        """
        Set up the necessary instances for each test method.
        """
        self.student_service = StudentService()

    @patch('converters.sql_converters.student_sql_converter.StudentSqlConverter')
    @patch('repositories.student_repository.StudentRepository')
    def test_save_all(self, mock_student_repository, mock_student_sql_converter):
        """
        Test the save_all method of StudentService.

        Mocks the dependencies and checks if the appropriate methods are called.
        """
        students = [
            Student(id=1, name='John Doe', birthday='2011-08-22T00:00:00.000000', room='2', sex='F'),
            Student(id=1, name='Jo Doex', birthday='2012-08-22T00:00:00.000000', room='3', sex='M')
        ]

        mock_converter_instance = mock_student_sql_converter.return_value
        mock_repository_instance = mock_student_repository.return_value
        self.student_service.student_sql_converter = mock_converter_instance
        self.student_service.student_repository = mock_repository_instance
        self.student_service.save_all(students)
        mock_converter_instance.convert_models_to_sql.assert_called_once_with(students)
        mock_repository_instance.save_students.assert_called_once()

    @patch('converters.sql_converters.student_sql_converter.StudentSqlConverter')
    @patch('repositories.student_repository.StudentRepository')
    def test_get_all(self, mock_student_repository, mock_student_sql_converter):
        """
        Test the get_all method of StudentService.

        Mocks the dependencies and checks if the appropriate methods are called.
        """
        mock_converter_instance = mock_student_sql_converter.return_value
        mock_repository_instance = mock_student_repository.return_value
        self.student_service.student_sql_converter = mock_converter_instance
        self.student_service.student_repository = mock_repository_instance
        result = self.student_service.get_all()
        mock_repository_instance.get_all.assert_called_once()
        mock_converter_instance.convert_sql_to_models.assert_called_once()
        self.assertEqual(result, mock_converter_instance.convert_sql_to_models.return_value)

    @patch('converters.type_converters.type_converter.TypeConverter')
    def test_save_to_file(self, mock_type_converter):
        """
        Test the save_to_file method of StudentService.

        Mocks the dependencies and checks if the appropriate methods are called.
        """
        students = [
            Student(id=1, name='John Doe', birthday="2011-08-22T00:00:00.000000", room=473, sex="M"),
            Student(id=2, name='John Doe', birthday="2011-08-22T00:00:00.000000", room=473, sex="M"),
        ]
        convert_type = ConvertType.JSON
        mock_converter_instance = mock_type_converter.return_value
        self.student_service.type_converter = mock_converter_instance
        self.student_service.save_to_file(students, convert_type)
        mock_converter_instance.convert.assert_called_once_with(students, convert_type)


if __name__ == '__main__':
    unittest.main()
