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
        if type(value) != int:
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

    def my_print(self):
        """
        Print the square with '#' characters.

        If the size is 0, this method prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
