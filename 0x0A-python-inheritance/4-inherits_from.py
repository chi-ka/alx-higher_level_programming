#!/usr/bin/python3
"""Returns True if the object is an instance of the specified class"""


def inherits_from(obj, a_class):
    """
    Checks if obj is an instance of class a_class.

    Returns: True if the object is an instance of the class
    and false otherwise.
    """
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
