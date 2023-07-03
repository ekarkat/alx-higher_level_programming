#!/usr/bin/python3
"""This is a rectangle Class"""


class Rectangle ():
    """Class triangle"""
    __width = None
    __height = None

    """Init class methof"""
    def __init__(self, width=0, height=0):
        """Init class methof"""
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Return height'''
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
