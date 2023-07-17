#!/usr/bin/python3
"""Rectangle Mosule"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """init function"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Return size"""
        return self.__width

    @size.setter
    def size(self, value):
        """set size"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value
        self.__height = value

    def __str__(self):
        """print str"""
        outpt = "[Square] ({}) {}/{} - {}".format(self.id,
                                                  self.x,
                                                  self.y,
                                                  self.width)
        return outpt
