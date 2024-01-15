from converters.sql_converters.sql_converter import ModelSqlConverter
from models.student import Student


class StudentSqlConverter(ModelSqlConverter):

    def _convert_model(self, model: Student) -> tuple:
        return (model.birthday, model.id, model.name, model.room, model.sex)

    def _convert_sql_to_model(self, sql_model: tuple) -> Student:
        return Student(sql_model[1], sql_model[2], sql_model[0], sql_model[3], sql_model[4])
