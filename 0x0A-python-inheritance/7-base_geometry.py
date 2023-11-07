#!/usr/bin/python3
"""Create an empty class BaseGeometry"""


class BaseGeometry():
    """
    An empty class BaseGeometry.

    """

    def area(self):
        """Empty Function area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
