from json_reader.json_reader import JsonReader
from models.room import Room


class RoomsJsonReader(JsonReader):

    def _get_model_hook(self):
        return lambda values: Room(**values)
