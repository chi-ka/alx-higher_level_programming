#!/usr/bin/python3
"""a class MyInt that inherits from int"""


class MyInt(int):
    """
    An class MyInt from int.
    """
    def __init__(self, num):
        """Initialiizng Class"""
        self.__num = num

    def __eq__(self, other):
        # Invert the == operator
        return not super().__eq__(other)

    def __ne__(self, other):
        # Invert the != operator
        return not super().__ne__(other)
