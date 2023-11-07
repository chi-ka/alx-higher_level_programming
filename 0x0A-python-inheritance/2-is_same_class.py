#!/usr/bin/python3
"""Returns True if the object is an instance of the specified class"""


def is_same_class(obj, a_class):
    """
    Checks if obj is an instance of class a_class.
    
    Returns: True if the object is an instance of the class
    """
    return (type(obj) is a_class)
