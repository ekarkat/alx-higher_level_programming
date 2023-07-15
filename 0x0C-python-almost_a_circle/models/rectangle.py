#!/usr/bin/python3
"""Rectangle Mosule"""

from models.base import Base


class Rectangle(Base):
    """The base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init function"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if type(value) == int:
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Return height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if type(value) == int:
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """Return X"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x"""
        if type(value) == int:
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """Return y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y"""
        if type(value) == int:
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value
        else:
            raise TypeError("y must be an integer")
