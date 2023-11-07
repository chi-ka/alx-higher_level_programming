#!/usr/bin/python3
"""function that returns the list of available attributes"""


def lookup(obj):
    """
    Returns a list of available attributes of an object.

    Returns:
    list: A list of attribute names of the object.
    """
    return [attr for attr in dir(obj)]
