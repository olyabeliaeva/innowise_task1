from typing import List

from repositories.base_repository import BaseRepository


class StudentRepository(BaseRepository):

    def save_students(self, sql_models: List[tuple]):
        with self.connection.cursor() as cursor:
            cursor.executemany(
                'INSERT INTO students(birthday,id,name,room,sex) VALUES (%s,%s,%s,%s,%s) ',
                sql_models)
        self.connection.commit()

    def get_all(self) -> List[tuple]:
        with self.connection.cursor() as cursor:
            cursor.execute('SELECT * FROM students')
            values = cursor.fetchall()
            return values
