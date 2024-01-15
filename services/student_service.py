import logging
from typing import List

from constants.type_constants import ConvertType
from converters.sql_converters.student_sql_converter import StudentSqlConverter
from converters.type_converters.type_converter import TypeConverter
from models.student import Student
from repositories.student_repository import StudentRepository


class StudentService():
    def __init__(self):
        self.student_sql_converter = StudentSqlConverter()
        self.student_repository = StudentRepository()
        self.type_converter = TypeConverter()

    def save_all(self, students: List[Student]):
        sql_model = self.student_sql_converter.convert_models_to_sql(students)
        self.student_repository.save_students(sql_model)
        logging.info('Students successfully saved to the DB')

    def get_all(self) -> List[Student]:
        logging.info('Start getting data about students from DB')
        sql_models = self.student_repository.get_all()
        return self.student_sql_converter.convert_sql_to_models(sql_models)

    def save_to_file(self, models: List[Student], convert_type: ConvertType):
        self.type_converter.convert(models, convert_type)
        logging.info('File with students succsessfully saved')
