from models.room import Room


class QueryModel(Room):
    def __init__(self, id, name, info):
        super().__init__(id, name)
        self.info = info
