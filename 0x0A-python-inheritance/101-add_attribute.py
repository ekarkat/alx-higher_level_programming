#!/usr/bin/python3
"""Module 101"""


def add_attribute(obj, attribute, value):
    """adds a new attribute to an object"""
    if '__dict__' in dir(obj):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
