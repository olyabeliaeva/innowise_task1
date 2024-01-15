import unittest
from unittest.mock import patch

from constants.type_constants import ConvertType
from models.room import Room
from services.room_service import RoomService


class RoomServiceTest(unittest.TestCase):

    def setUp(self):
        self.room_service = RoomService()

    @patch('converters.sql_converters.room_sql_converter.RoomSqlConverter')
    @patch('repositories.room_repository.RoomRepository')
    def test_save_all(self, mock_room_repository, mock_room_sql_converter):
        rooms = [
            Room(id=1, name='Room #1'),
            Room(id=2, name='Room #2')
        ]

        mock_converter_instance = mock_room_sql_converter.return_value
        mock_repository_instance = mock_room_repository.return_value
        self.room_service.room_sql_converter = mock_converter_instance
        self.room_service.room_repository = mock_repository_instance
        self.room_service.save_all(rooms)
        mock_converter_instance.convert_models_to_sql.assert_called_once_with(rooms)
        mock_repository_instance.save_rooms.assert_called_once()

    @patch('converters.sql_converters.room_sql_converter.RoomSqlConverter')
    @patch('repositories.room_repository.RoomRepository')
    def test_get_all(self, mock_room_repository, mock_room_sql_converter):
        mock_converter_instance = mock_room_sql_converter.return_value
        mock_repository_instance = mock_room_repository.return_value
        self.room_service.room_sql_converter = mock_converter_instance
        self.room_service.room_repository = mock_repository_instance
        result = self.room_service.get_all()
        mock_repository_instance.get_all.assert_called_once()
        mock_converter_instance.convert_sql_to_models.assert_called_once()
        self.assertEqual(result, mock_converter_instance.convert_sql_to_models.return_value)

    @patch('converters.type_converters.type_converter.TypeConverter')
    def test_save_to_file(self, mock_type_converter):
        rooms = [
            Room(id=1, name='Room #1'),
            Room(id=2, name='Room #2')
        ]
        convert_type = ConvertType.JSON
        mock_converter_instance = mock_type_converter.return_value
        self.room_service.type_converter = mock_converter_instance
        self.room_service.save_to_file(rooms, convert_type)
        mock_converter_instance.convert.assert_called_once_with(rooms, convert_type)


if __name__ == '__main__':
    unittest.main()
