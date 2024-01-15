from models.base_model import BaseModel


class Student(BaseModel):
    def __init__(self, id, name, birthday, room, sex):
        super().__init__(id, name)
        self.birthday = birthday
        self.room = room
        self.sex = sex

    def __str__(self):
        return f' {super().__str__()},{self.birthday},{self.room},{self.sex}'
