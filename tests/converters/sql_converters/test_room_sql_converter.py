import unittest

from converters.sql_converters.room_sql_converter import RoomSqlConverter
from models.room import Room


class TestRoomSqlConverter(unittest.TestCase):
    """
    Unit tests for the RoomSqlConverter class.

    This class inherits from unittest.TestCase and contains two test methods:
    - test__convert_model: Tests the _convert_model method of RoomSqlConverter.
    - test__convert_sql_to_model: Tests the _convert_sql_to_model method of RoomSqlConverter.
    """

    def test__convert_model(self):
        """
        Test the _convert_model method of RoomSqlConverter.

        Creates a test Room instance, converts it to a SQL model, and compares the result with the expected outcome.
        """
        test_room = Room(
            id=1,
            name='Room #1'
        )

        room_sql_converter = RoomSqlConverter()
        result = room_sql_converter._convert_model(test_room)
        expected_result = (1, 'Room #1')
        self.assertEqual(result, expected_result)

    def test__convert_sql_to_model(self):
        """
        Test the _convert_sql_to_model method of RoomSqlConverter.

        Creates a test SQL model, converts it to a Room instance, and compares the result with the expected outcome.
        """
        test_sql_model = (69, 'Room #69')
        room_sql_converter = RoomSqlConverter()
        room = room_sql_converter._convert_sql_to_model(test_sql_model)

        self.assertEqual(room.id, 69)
        self.assertEqual(room.name, 'Room #69')


if __name__ == '__main__':
    unittest.main()
