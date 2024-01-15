import os

import psycopg2


class DatabaseConfiguration():
    host = os.getenv('DB_HOST')
    db_name = os.getenv('DB_NAME')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')

    def __init__(self):
        self.connection = psycopg2.connect(
            host=self.host,
            database=self.db_name,
            user=self.user,
            password=self.password
        )
