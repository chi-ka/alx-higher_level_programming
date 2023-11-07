#!/usr/bin/python3
"""Create an empty class BaseGeometry"""


class BaseGeometry():
    """
    An empty class BaseGeometry.

    """

    def area(self):
        """Empty Function area"""
        pass

    def integer_validator(self, name, value):
        """Validate an integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """
    An class inherited from BaseGeometry.

    """
    def __init__(self, width, height):
        """Initialiizng Class"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Get's the area of a Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the sring"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

class Square(Rectangle):
    """
    A class inherited from Rectangle.

    """
    def __init__(self, size):
        Rectangle.__init__(self, size, size)
        """ Initializing the square"""
        self.integer_validator('size', size)
        self.__size = size
        
    def area(self):
        """ Get's the area of a square"""
        return self.__size * 2
        
    def __str__(self):
        """Return the sring when print is called"""
        return "[Square] {}/{}".format(self.__size, self.__size)
