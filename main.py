import argparse

from configurations.logger_configuration import LOGGER
from constants.type_constants import ConvertType
from json_reader.rooms_json_reader import RoomsJsonReader
from json_reader.students_json_reader import StudentsJsonReader
from services.queries_service import QueriesService
from services.room_service import RoomService
from services.student_service import StudentService

queries_service = QueriesService()
choise_to_query = {
    '1': queries_service.get_list_of_rooms_with_quantity_students,
    '2': queries_service.get_five_rooms_with_min_avg_age_of_students,
    '3': queries_service.get_five_rooms_with_max_difference_age_of_students,
    '4': queries_service.get_list_of_rooms_includes_students_with_different_sexes
}


def main():
    """
    Main entry point for the script.

    Parses command-line arguments, reads data from JSON files, performs queries,
    and saves the results in the specified output format.

    Usage: python main.py --students-json students.json --rooms-json rooms.json --query 1 --output-format JSON/XML
    """
    parser = argparse.ArgumentParser(description='Command-line interface for reading and saving data')

    parser.add_argument('--rooms-json', help='Path to rooms JSON file')
    parser.add_argument('--students-json', help='Path to students JSON file')
    parser.add_argument('--query', choices=['1', '2', '3', '4'], help='Read description about queries in README')
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
    query_model = choise_to_query[args.query]()
    queries_service.save_to_file(query_model, ConvertType[args.output_format])
    rooms_data = room_service.get_all()
    room_service.save_to_file(rooms_data, ConvertType[args.output_format])
    students_data = student_service.get_all()
    student_service.save_to_file(students_data, ConvertType[args.output_format])

    LOGGER.info('Finish script!')


if __name__ == '__main__':
    main()
