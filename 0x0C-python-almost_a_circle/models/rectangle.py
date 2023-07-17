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

    def area(self):
        """Return area of rectangle"""
        area = self.height * self.width
        return area

    def display(self):
        """prints the Rectangle with the character # """

        for y in range(self.y):
            print("")
        for row in range(self.height):
            for x in range(self.x):
                print(" ", end='')
            for lin in range(self.width):
                print("#", end='')
            print("")

    def __str__(self):
        """print str function"""
        outpt = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                        self.x,
                                                        self.y,
                                                        self.width,
                                                        self.height
                                                        )
        return outpt

    def update(self, *args, **kwargs):
        """update Rectangle"""
        if len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.width = args[1]
                elif i == 2:
                    self.height = args[2]
                elif i == 3:
                    self.x = args[3]
                elif i == 4:
                    self.y = args[4]

        if kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
