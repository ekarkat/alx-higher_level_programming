#!/usr/bin/python3
'''Module 6'''


class Student():
    """Class Student"""

    first_name = ""
    last_name = ""
    age = None

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            for key in attrs:
                if type(key) is str:
                    continue
                return self.__dict__
            liste = {}
            for key in attrs:
                if key in self.__dict__.keys():
                    liste[key] = self.__dict__[key]
            return liste
        else:
            return self.__dict__

    def reload_from_json(self, json):
        self.first_name = json.get("first_name")
        self.last_name = json.get("last_name")
        self.age = json.get("age")
