from typing import List

from repositories.base_repository import BaseRepository


class QueriesRepository(BaseRepository):
    """
    A repository class for executing various SQL queries related to rooms and students.

    This class inherits from BaseRepository.

    Methods:
        get_list_of_rooms_with_quantity_students() -> List[tuple]:
            Retrieve a list of rooms with the quantity of students in each room.

        get_five_rooms_with_min_avg_age_of_students() -> List[tuple]:
            Retrieve five rooms with the minimum average age of students.

        get_five_rooms_with_max_difference_age_of_students() -> List[tuple]:
            Retrieve five rooms with the maximum difference in age among students.

        get_list_of_rooms_includes_students_with_different_sexes() -> List[tuple]:
            Retrieve a list of rooms that include students with different sexes.

        get_creating_indexes_for_optimisation_queries() -> None:
            Execute a SQL query to create indexes for optimization purposes.
    """

    def get_list_of_rooms_with_quantity_students(self) -> List[tuple]:
        """
        Retrieve a list of rooms with the quantity of students in each room.

        Returns:
            List[tuple]: The result of the query as a list of tuples.
        """
        query = 'SELECT rooms.id, rooms.name, COUNT(students.id) ' \
                'FROM rooms ' \
                'JOIN students ON rooms.id = students.room ' \
                'GROUP BY rooms.id ' \
                'ORDER BY rooms.id;'
        return self.execute_query_to_db(query)

    def get_five_rooms_with_min_avg_age_of_students(self) -> List[tuple]:
        """
        Retrieve five rooms with the minimum average age of students.

        Returns:
            List[tuple]: The result of the query as a list of tuples.
        """
        query = 'SELECT rooms.id, rooms.name, avg(EXTRACT(EPOCH FROM birthday)) as avg_birthday ' \
                'FROM rooms ' \
                'JOIN students s on rooms.id = s.room ' \
                'GROUP BY rooms.id ' \
                'ORDER BY avg_birthday desc ' \
                'LIMIT (5);'
        return self.execute_query_to_db(query)

    def get_five_rooms_with_max_difference_age_of_students(self) -> List[tuple]:
        """
        Retrieve five rooms with the maximum difference in age among students.

        Returns:
            List[tuple]: The result of the query as a list of tuples.
        """
        query = 'SELECT rooms.id, rooms.name, ' \
                '(max(EXTRACT(EPOCH FROM birthday)) - min(EXTRACT(EPOCH FROM birthday))) as diff_age ' \
                'FROM rooms ' \
                'JOIN students s on rooms.id = s.room ' \
                'GROUP BY rooms.id ' \
                'ORDER BY diff_age DESC ' \
                'LIMIT (5);'
        return self.execute_query_to_db(query)

    def get_list_of_rooms_includes_students_with_different_sexes(self) -> List[tuple]:
        """
        Retrieve a list of rooms that include students with different sexes.

        Returns:
            List[tuple]: The result of the query as a list of tuples.
        """
        query = 'SELECT rooms.id, rooms.name ' \
                'FROM rooms ' \
                'JOIN students ON rooms.id = students.room ' \
                'GROUP BY rooms.id ' \
                'HAVING COUNT(DISTINCT students.sex) > 1;'
        return self.execute_query_to_db(query)

    def get_creating_indexes_for_optimisation_queries(self) -> None:
        """
        Execute a SQL query to create indexes for optimization purposes.

        Returns:
            None
        """
        query = 'CREATE INDEX idx_room_id  ON rooms(id), students(room)'
        return self.execute_creating_indexes(query)
