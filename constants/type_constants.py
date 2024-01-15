from enum import Enum


class ConvertType(Enum):
    """
    An enumeration representing different types of data conversion formats.

    Enum Members:
        JSON (str): Represents the JSON data format.
        XML (str): Represents the XML data format.
    """

    JSON = 'JSON'
    XML = 'XML'
