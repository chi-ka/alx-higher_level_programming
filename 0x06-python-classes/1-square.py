#!/usr/bin/python3
class Square:
    """
    This is a simple class that defines a square.

    The Square class is used to represent a square shape with a single attribute,
    '__size', which stores the size of all sides of the square. The '__size' attribute
    is encapsulated using double underscores to make it a private attribute.
    """
    def __init__(self, size):
        self.__size = size
