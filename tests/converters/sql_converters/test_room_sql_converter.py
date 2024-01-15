import unittest

from converters.sql_converters.room_sql_converter import RoomSqlConverter
from models.room import Room


class TestRoomSqlConverter(unittest.TestCase):

    def test__convert_model(self):
        test_student = Room(
            id=1,
            name='Room #1'
        )

        room_sql_converter = RoomSqlConverter()
        result = room_sql_converter._convert_model(test_student)
        expected_result = (1, 'Room #1')
        self.assertEqual(result, expected_result)

    def test__convert_sql_to_model(self):
        test_sql_model = (69, 'Room #69')
        room_sql_converter = RoomSqlConverter()
        room = room_sql_converter._convert_sql_to_model(test_sql_model)

        self.assertEqual(room.id, 69)
        self.assertEqual(room.name, 'Room #69')


if __name__ == '__main__':
    unittest.main()
