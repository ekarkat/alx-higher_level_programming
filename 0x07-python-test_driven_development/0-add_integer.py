"""a function that adds 2 integers"""


def add_integer(a, b=98):
    """ Result of a + b"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not float and type(b) is not int:
        raise TypeError("b must be an integer")

    sum = int(a) + int(b)
    return (sum)
