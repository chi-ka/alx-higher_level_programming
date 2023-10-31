#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """
    Defines a rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle object with optional width and height.

        Args:
            width (int, optional): The width of the Rectangle. Defaults to 0.
            height (int, optional): The height of the Rectangle. Defaults to 0.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Retrieve the width property.
        """
        return self.__width

    @property
    def height(self):
        """
        Retrieve the height property.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            ValueError: If width is less than 0.
            TypeError: If width is not an integer.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            ValueError: If height is less than 0.
            TypeError: If height is not an integer.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Calculate and return the area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.
        """
        if self.__height == 0 or self.height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        Return a string representation of the rectangle.
        Returns:
        str: A string representing the rectangle using '#' characters.
        """
        if self.__height == 0 or self.__width == 0:
            return ""

        rectangle_str = ""

        for i in range(self.__height):
            for j in range(self.__width):
                if j == (self.__width - 1):
                    rectangle_str += "#\n"
                else:
                    rectangle_str += "#"

        return rectangle_str
