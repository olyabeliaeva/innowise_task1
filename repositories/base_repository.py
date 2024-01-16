from abc import ABC
from typing import List

from configurations.database_configuration import DatabaseConfiguration


class BaseRepository(ABC):
    """
    An abstract base class for defining common database operations.

    Attributes:
        db_config (DatabaseConfiguration): The database configuration instance.
        connection: The database connection instance.
    """

    db_config = DatabaseConfiguration()

    def __init__(self):
        """
        Initialize a new instance of the BaseRepository class.
        Establish a connection to the database.
        """
        self.connection = self.db_config.connection

    def execute_query_to_db(self, query: str) -> List[tuple]:
        """
        Execute a SQL query and fetch the results from the database.

        Args:
            query (str): The SQL query to be executed.

        Returns:
            List[tuple]: The result of the query as a list of tuples.
        """
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            values = cursor.fetchall()
            return values

    def execute_queries_to_db(self, query: str, sql_models: List[tuple]) -> None:
        """
        Execute multiple SQL queries with parameterized values and commit the changes to the database.

        Args:
            query (str): The parameterized SQL query to be executed.
            sql_models (List[tuple]): The list of tuples containing values for the parameterized query.
        """
        with self.connection.cursor() as cursor:
            cursor.executemany(query, sql_models)
        self.connection.commit()

    def execute_creating_indexes(self, query: str) -> None:
        """
        Execute a SQL query for creating indexes and commit the changes to the database.

        Args:
            query (str): The SQL query for creating indexes.
        """
        with self.connection.cursor() as cursor:
            cursor.execute(query)
        self.connection.commit()
