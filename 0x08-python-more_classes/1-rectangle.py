#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """
        Defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """
            Initialize a Rectangle object with an optional size.
        
            Args:
                width (int, optional): The width of the Rectangle. Defaults to 0.
                height (int, optional): The height of the Rectangle Defaults to 0.
    
        """
        self.__width = width
        self.__height = height
        
    @property
    def width(self):
        """
            Retrives the width property
        """
        return self.__width
        
    @property
    def height(self):
        """
            Retrives the height property
        """
        return self.__height
    
    @width.setter
    def width(self, value):
        """
            Set the width of the square.
        
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
            self.__width = value
            
    @height.setter
    def height(self, value):
        """
            Set the height of the square.
        
            Args:
                value (int): The new size of the square.
        
            Raises:
                ValueError: If size is less than 0.
                TypeError: If size is not an integer.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
