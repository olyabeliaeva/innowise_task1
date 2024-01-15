from models.base_model import BaseModel


class Room(BaseModel):
    def __init__(self, id, name):
        super().__init__(id, name)
