from converters.sql_converters.sql_converter import ModelSqlConverter
from models.student import Student


class StudentSqlConverter(ModelSqlConverter):
    """
    A SQL converter for converting between Student instances and their corresponding SQL representation.

    This class inherits from ModelSqlConverter.

    Methods:
        _convert_model(model: Student) -> tuple:
            Convert a Student instance to its SQL representation.

        _convert_sql_to_model(sql_model: tuple) -> Student:
            Convert a SQL representation (tuple) to a Student instance.
    """

    def _convert_model(self, model: Student) -> tuple:
        """
        Convert a Student instance to its SQL representation.

        Args:
            model (Student): The Student instance to be converted.

        Returns:
            tuple: The SQL representation of the Student instance.
        """
        return (model.birthday, model.id, model.name, model.room, model.sex)

    def _convert_sql_to_model(self, sql_model: tuple) -> Student:
        """
        Convert a SQL representation (tuple) to a Student instance.

        Args:
            sql_model (tuple): The SQL representation of a Student instance.

        Returns:
            Student: The Student instance created from the SQL representation.
        """
        return Student(sql_model[1], sql_model[2], sql_model[0], sql_model[3], sql_model[4])
