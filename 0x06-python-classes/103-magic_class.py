"""A magical class for performing calculations"""


import math
"""A magical class for performing calculations"""

class MagicClass:
    """
    A magical class for performing calculations on circles.

    Attributes:
        __radius (int or float): The radius of the circle.

    Methods:
        __init__(self, radius=0): Initializes a MagicClass instance with a specified radius.
        area(self): Calculates and returns the area of the circle.
        circumference(self): Calculates and returns the circumference of the circle.
    """

    def __init__(self, radius=0):
        """
        Initialize a MagicClass instance with a specified radius.

        Args:
            radius (int or float, optional): The radius of the circle. Defaults to 0.

        Raises:
            TypeError: If the radius is not a number (int or float).
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculate and return the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate and return the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius

