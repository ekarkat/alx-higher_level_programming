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

    @classmethod
    def save_to_file(cls, list_objs):
        """Save to json file"""
        file_name = cls.__name__ + ".json"
        list_dict = []
        if list_objs is not None:
            for item in list_objs:
                list_dict.append(item.to_dictionary())
        with open(file_name, "w") as f:
            f.write(Base.to_json_string(list_dict))
