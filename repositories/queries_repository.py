from repositories.base_repository import BaseRepository


class QueriesRepository(BaseRepository):

    def get_list_of_rooms_with_quantity_students(self):
        with self.connection.cursor() as cursor:
            cursor.execute('SELECT rooms.id , rooms.name , COUNT(students.id) '
                           'From rooms '
                           'JOIN students ON rooms.id =students.room '
                           'GROUP BY rooms.id '
                           'ORDER BY rooms.id;')
            values = cursor.fetchall()
            return values

    def get_five_rooms_with_min_avg_age_of_students(self):
        with self.connection.cursor() as cursor:
            cursor.execute('SELECT  rooms.id, rooms.name, avg(EXTRACT(EPOCH FROM birthday)) as avg_birthday '
                           'FROM rooms '
                           'JOIN students s on rooms.id = s.room '
                           'GROUP BY rooms.id '
                           'ORDER BY avg_birthday desc '
                           'LIMIT (5);')
            values = cursor.fetchall()
            return values

    def get_five_rooms_with_max_difference_age_of_students(self):
        with self.connection.cursor() as cursor:
            cursor.execute('SELECT rooms.id,rooms.name, '
                           '(max(EXTRACT(EPOCH FROM birthday)) - min(EXTRACT(EPOCH FROM birthday))) as diff_age '
                           'FROM rooms '
                           'JOIN students s on rooms.id = s.room '
                           'GROUP BY rooms.id '
                           'ORDER BY diff_age DESC '
                           'LIMIT (5);')
            values = cursor.fetchall()
            return values

    def get_list_of_rooms_includes_students_with_different_sexes(self):
        with self.connection.cursor() as cursor:
            cursor.execute('SELECT rooms.id, rooms.name '
                           'FROM rooms '
                           'JOIN students ON rooms.id = students.room '
                           'GROUP BY rooms.id '
                           'HAVING COUNT(DISTINCT students.sex) > 1;')
            values = cursor.fetchall()
            return values

    def get_creating_indexes_for_optimisation_querries(self):
        with self.connection.cursor() as cursor:
            cursor.execute('CREATE INDEX idx_room_id  ON rooms(id), students(room)')
            self.connection.commit()
