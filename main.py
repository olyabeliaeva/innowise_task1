import argparse

from configurations.logger_configuration import LOGGER
from constants.type_constants import ConvertType
from json_reader.rooms_json_reader import RoomsJsonReader
from json_reader.students_json_reader import StudentsJsonReader
from services.room_service import RoomService
from services.student_service import StudentService

# script: python main.py --students-json students.json --rooms-json rooms.json --output-format JSON

def main():
    parser = argparse.ArgumentParser(description='Command-line interface for reading and saving data.')

    parser.add_argument('--rooms-json', help='Path to rooms JSON file')
    parser.add_argument('--students-json', help='Path to students JSON file')
    parser.add_argument('--output-format', choices=['JSON', 'XML'], help='Output format (json or xml)')

    args = parser.parse_args()

    LOGGER.info('Start script!')
    rooms_reader = RoomsJsonReader()
    students_reader = StudentsJsonReader()
    rooms = rooms_reader.read_json(args.rooms_json)
    students = students_reader.read_json(args.students_json)

    room_service = RoomService()
    student_service = StudentService()
    room_service.save_all(rooms)
    student_service.save_all(students)

    rooms_data = room_service.get_all()
    room_service.save_to_file(rooms_data, ConvertType[args.output_format])
    students_data = student_service.get_all()
    student_service.save_to_file(students_data, ConvertType[args.output_format])
    LOGGER.info('Finish script!')


if __name__ == '__main__':
    main()
