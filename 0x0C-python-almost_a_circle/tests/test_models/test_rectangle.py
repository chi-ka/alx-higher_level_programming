#!/usr/bin/python3
import unittest
import os
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base

class TestRectangle(unittest.TestCase):
    def test_init(self):
        rectangle = Rectangle(10, 20, 1, 2, 3)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 2)
        self.assertEqual(rectangle.id, 3)

    def test_width_setter(self):
        rectangle = Rectangle(5, 10)
        rectangle.width = 15
        self.assertEqual(rectangle.width, 15)

if __name__ == '__main__':
    unittest.main()
