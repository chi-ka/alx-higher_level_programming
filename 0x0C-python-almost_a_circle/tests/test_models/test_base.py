#!/usr/bin/python3
import unittest
import os
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base

class TestBase(unittest.TestCase):
    def test_create(self):
        dictionary = {'width': 5, 'height': 10, 'x': 2, 'y': 3, 'id': 4}
        rectangle = Base.create(**dictionary)
        self.assertIsInstance(rectangle, Rectangle)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)
        self.assertEqual(rectangle.id, 4)

if __name__ == '__main__':
    unittest.main()
