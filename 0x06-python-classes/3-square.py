#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        """
        Initialize a Square object with an optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            ValueError: If size is less than 0.
            TypeError: If size is not an integer.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return(self.__size**2)
