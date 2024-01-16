import logging
from typing import List

from converters.sql_converters.student_sql_converter import StudentSqlConverter
from converters.type_converters.type_converter import TypeConverter
from models.student import Student
from repositories.student_repository import StudentRepository
from services.base_service import BaseService


class StudentService(BaseService):
    """
    A service class for handling operations related to students.

    This class inherits from BaseService.

    Attributes:
        student_sql_converter (StudentSqlConverter): An instance of the StudentSqlConverter class for converting between
                                                     Student instances and SQL models.
        student_repository (StudentRepository): An instance of the StudentRepository class
         for executing student-related queries.
        type_converter (TypeConverter): An instance of the TypeConverter class for converting models.

    Methods:
        save_all(students: List[Student]) -> None:
            Save a list of students to the database.

        get_all() -> List[Student]:
            Retrieve all students from the database.

    Usage:
        # Example usage to save and retrieve students:
        service = StudentService()
        service.save_all(list_of_students)
        students = service.get_all()
    """

    def __init__(self):
        """
        Initialize a new instance of the StudentService class.
        Create instances of the StudentSqlConverter, StudentRepository, and TypeConverter classes.
        """
        super(StudentService, self).__init__()
        self.student_sql_converter = StudentSqlConverter()
        self.student_repository = StudentRepository()
        self.type_converter = TypeConverter()

    def save_all(self, students: List[Student]) -> None:
        """
        Save a list of students to the database.

        Args:
            students (List[Student]): The list of Student instances to be saved.

        Returns:
            None
        """
        sql_models = self.student_sql_converter.convert_models_to_sql(students)
        self.student_repository.save_students(sql_models)
        logging.info('Students successfully saved to the DB')

    def get_all(self) -> List:
        """
        Retrieve all students from the database.

        Returns:
            List[Student]: The result of the query as a list of Student instances.
        """
        logging.info('Start getting data about students from DB')
        sql_models = self.student_repository.get_all()
        return self.student_sql_converter.convert_sql_to_models(sql_models)
