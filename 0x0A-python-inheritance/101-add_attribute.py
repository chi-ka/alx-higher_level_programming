#!/usr/bin/python3
""" A function that adds a new attribute to an object"""

def add_attribute(obj, attr, value):
    """adds a new attribute"""
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
