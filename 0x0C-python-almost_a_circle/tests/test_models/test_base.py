#!/usr/bin/python3
'''Base class tests'''


import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):
    def test_ids(self):
        """Test ids"""

        base1 = Base()
        base2 = Base(7)
        base3 = Base()
        base4 = Base(89)

        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 7)
        self.assertEqual(base3.id, 2)
        self.assertEqual(base4.id, 89)


