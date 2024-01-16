class BaseModel:
    """
    A base class for representing common attributes and methods of models.

    Attributes:
        id: Identifier for the model.
        name: Name associated with the model.
    """

    def __init__(self, id, name):
        """
        Initialize a new instance of the BaseModel class.

        Args:
            id: Identifier for the model.
            name: Name associated with the model.
        """
        self.id = id
        self.name = name

    def __str__(self) -> str:
        """
        Return a string representation of the model.

        Returns:
            str: A string representation of the model in the format 'id, name'.
        """
        return f'{self.id},{self.name}'
