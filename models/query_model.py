from models.room import Room


class QueryModel(Room):
    """
    A model class representing query-specific information, inheriting from the Room model.

    Attributes:
        id: Identifier for the query model.
        name: Name associated with the query model.
        info: Additional information specific to the query model.
    """

    def __init__(self, id, name, info):
        """
        Initialize a new instance of the QueryModel class.

        Args:
            id: Identifier for the query model.
            name: Name associated with the query model.
            info: Additional information specific to the query model.
        """
        super().__init__(id, name)
        self.info = info
