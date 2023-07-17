#!/usr/bin/python3
"""Base Mosule"""
import json


class Base():
    """The base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init function"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return json string"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
