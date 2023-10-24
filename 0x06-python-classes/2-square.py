#!/usr/bin/python3
class Square:
    """
    This class represents a square.

    A Square object is defined by its size, which is an integer as
    the length of all sides of the square. The size is
    encapsulated as a private attribute '__size'.

    """

    def __init__(self, size=0):
        """
        Initialize a new Square with a given size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            ValueError: If the provided size is less than 0.
            TypeError: If the provided size is not an integer.
        """
        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
