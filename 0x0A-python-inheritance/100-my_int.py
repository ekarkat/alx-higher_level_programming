#!/usr/bin/python3
"""Module 100"""


class MyInt(int):
    """MyInt is a rebel. MyInt has == and != operators inverted"""

    def __init__(self, num):
        self.num = num

    def __eq__(self, value):
        if self.num != value:
            return True
        return False

    def __ne__(self, value):
        if self.num == value:
            return True
        return False
