from models.base_model import BaseModel


class Student(BaseModel):
    """
    A model class representing students, inheriting from the BaseModel.

    Attributes:
        id: Identifier for the student.
        name: Name associated with the student.
        birthday: Birthday of the student.
        room: Room associated with the student.
        sex: Gender of the student.
    """

    def __init__(self, id, name, birthday, room, sex):
        """
        Initialize a new instance of the Student class.

        Args:
            id: Identifier for the student.
            name: Name associated with the student.
            birthday: Birthday of the student.
            room: Room associated with the student.
            sex: Gender of the student.
        """
        super().__init__(id, name)
        self.birthday = birthday
        self.room = room
        self.sex = sex

    def __str__(self):
        """
        Return a string representation of the student.

        Returns:
            str: A string representation of the student in the format 'id, name, birthday, room, sex'.
        """
        return f' {super().__str__()},{self.birthday},{self.room},{self.sex}'
