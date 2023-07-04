#!/usr/bin/python3
"""This is a rectangle Class"""


class Rectangle ():
    """Class triangle"""

    number_of_instances = 0
    print_symbol = "#"

    """Init class methof"""
    def __init__(self, width=0, height=0):
        """Init class methof"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Return area"""
        area = (self.__height * self.__width)
        return area

    def perimeter(self):
        """Return perimetre"""
        if self.__width == 0 or self.__height == 0:
            return 0
        perimetre = (self.__width + self.height) * 2
        return perimetre

    def __str__(self):
        """ Prints rectangle with #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        shape = ""
        for i in range(self.__height):
            for j in range(self.__width):
                shape = shape + str(self.print_symbol)
            if i != self.__height - 1:
                shape = shape + "\n"
        return shape

    def __repr__(self):
        """ __repr__"""
        return ("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        """ Deletes  object """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
