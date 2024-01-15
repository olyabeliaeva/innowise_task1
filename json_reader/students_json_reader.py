from json_reader.json_reader import JsonReader
from models.student import Student


class StudentsJsonReader(JsonReader):

    def _get_model_hook(self):
        return lambda values: Student(**values)
