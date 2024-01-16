from models.base_model import BaseModel


class Room(BaseModel):
    """
    A model class representing rooms, inheriting from the BaseModel.

    Attributes:
        id: Identifier for the room.
        name: Name associated with the room.
    """

    def __init__(self, id, name):
        """
        Initialize a new instance of the Room class.

        Args:
            id: Identifier for the room.
            name: Name associated with the room.
        """
        super().__init__(id, name)
