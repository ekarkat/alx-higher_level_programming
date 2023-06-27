#!/usr/bin/python3
"""Modue Square"""


class Square:
    """ Square class """

    __size = None

    @property
    def size(self):
        return self.__size

    @size.setter
    def __init__(self, size=0):
        """ init class by size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
