#!/usr/bin/python3
'''Base class tests'''


import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleClass(unittest.TestCase):
    def test_init(self):
        """Task 2 and 3"""

        r1 = Rectangle(15, 12, 1, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 15)
        self.assertEqual(r1.height, 12)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 2)

        r2 = Rectangle()
        self.assertEqual(r2.id, 2)