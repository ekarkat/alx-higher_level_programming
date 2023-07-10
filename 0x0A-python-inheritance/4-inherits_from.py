#!/usr/bin/python3
"""Module 4"""


def inherits_from(obj, a_class):
    """ a function that returns True if the object
      is an instance of a class that inherited
      (directly or indirectly) from the specified class ; otherwise False."""

    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    return False
