from abc import ABC

from configurations.database_configuration import DatabaseConfiguration


class BaseRepository(ABC):
    db_config = DatabaseConfiguration()

    def __init__(self):
        self.connection = self.db_config.connection
