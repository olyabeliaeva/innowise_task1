from typing import List

from repositories.base_repository import BaseRepository


class RoomRepository(BaseRepository):
    """
    A repository class for executing SQL queries related to rooms.

    This class inherits from BaseRepository.

    Methods:
        save_rooms(sql_models: List[tuple]) -> None:
            Save rooms to the database.

        get_all() -> List[tuple]:
            Retrieve all rooms from the database.
    """

    def save_rooms(self, sql_models: List[tuple]) -> None:
        """
        Save rooms to the database.

        Args:
            sql_models (List[tuple]): The list of tuples containing values for the rooms.

        Returns:
            None
        """
        query = 'INSERT INTO rooms(id, name) VALUES (%s, %s);'
        return self.execute_queries_to_db(query, sql_models)

    def get_all(self) -> List[tuple]:
        """
        Retrieve all rooms from the database.

        Returns:
            List[tuple]: The result of the query as a list of tuples.
        """
        query = 'SELECT * FROM rooms;'
        return self.execute_query_to_db(query)
