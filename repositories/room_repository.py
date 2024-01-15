from typing import List

from repositories.base_repository import BaseRepository


class RoomRepository(BaseRepository):

    def save_rooms(self, sql_models: List[tuple]):
        with self.connection.cursor() as cursor:
            cursor.executemany('INSERT INTO rooms(id,name) VALUES (%s,%s) ', sql_models)
        self.connection.commit()

    def get_all(self) -> List[tuple]:
        with self.connection.cursor() as cursor:
            cursor.execute('SELECT * FROM rooms')
            values = cursor.fetchall()
            return values

    def add_indexes(self):
        with self.connection:
            with self.cursor:
                self.cursor.execute('CREATE * FROM rooms')
