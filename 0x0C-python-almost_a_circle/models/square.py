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
        return self.width

    @size.setter
    def size(self, value):
        """set size"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    def __str__(self):
        """print str"""
        outpt = "[Square] ({}) {}/{} - {}".format(self.id,
                                                  self.x,
                                                  self.y,
                                                  self.width)
        return outpt

    def update(self, *args, **kwargs):
        """update Square"""
        if len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.width = args[1]
                elif i == 2:
                    self.height = args[1]
                elif i == 3:
                    self.x = args[2]
                elif i == 4:
                    self.y = args[3]
        if kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
