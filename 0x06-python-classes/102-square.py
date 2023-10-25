#!/usr/bin/python3
"""This is a simple class that defines a square."""


class Square:
    """This is a simple class that defines a square."""

    def __init__(self, size=0):
        """
        Initialize a Square object with an optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            ValueError: If size is less than 0.
            TypeError: If size is not an integer.
        """
        self.size = size

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            ValueError: If size is less than 0.
            TypeError: If size is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Override the equality operator (==)."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Override the inequality operator (!=)."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Override the less than operator (<)."""
        return self.area() < other.area()

    def __le__(self, other):
        """Override the less than or equal to operator (<=)."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Override the greater than operator (>)."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Override the greater than or equal to operator (>=)."""
        return self.area() >= other.area()
