from typing import List

from repositories.base_repository import BaseRepository


class StudentRepository(BaseRepository):
    """
    A repository class for executing SQL queries related to students.

    This class inherits from BaseRepository.

    Methods:
        save_students(sql_models: List[tuple]) -> None:
            Save students to the database.

        get_all() -> List[tuple]:
            Retrieve all students from the database.
    """

    def save_students(self, sql_models: List[tuple]) -> None:
        """
        Save students to the database.

        Args:
            sql_models (List[tuple]): The list of tuples containing values for the students.

        Returns:
            None
        """
        query = 'INSERT INTO students(birthday, id, name, room, sex) VALUES (%s, %s, %s, %s, %s) '
        return self.execute_queries_to_db(query, sql_models)

    def get_all(self) -> List[tuple]:
        """
        Retrieve all students from the database.

        Returns:
            List[tuple]: The result of the query as a list of tuples.
        """
        query = 'SELECT * FROM students;'
        return self.execute_query_to_db(query)
