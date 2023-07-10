#!/usr/bin/python3
"""Module 10 square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square of subclass Rectangle"""
    def __init__(self, size):
        """init of square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        text = "[{}] {}/{}".format("Square",
                                   self.__width, self.__height)
        return text
