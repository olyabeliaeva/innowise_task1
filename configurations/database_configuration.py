import os

import psycopg2


class DatabaseConfiguration:
    """
    A class representing the configuration details for connecting to a PostgreSQL database.

    Attributes:
        host (str): The host address of the database.
        db_name (str): The name of the database.
        user (str): The username for connecting to the database.
        password (str): The password for connecting to the database.
        connection (psycopg2.extensions.connection): The connection object to the database.
    """

    host = os.getenv('DB_HOST')
    db_name = os.getenv('DB_NAME')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')

    def __init__(self):
        """
        Initializes a new instance of the DatabaseConfiguration class and establishes a connection
        to the PostgreSQL database using the provided configuration details.
        """
        self.connection = psycopg2.connect(
            host=self.host,
            database=self.db_name,
            user=self.user,
            password=self.password
        )
