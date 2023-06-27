#!/usr/bin/python3
"""Modue Square"""


class Square:
    """ Square class """

    __size = None

    def __init__(self, size=0) -> None:
        """ init class by size"""

        self.__size = size
