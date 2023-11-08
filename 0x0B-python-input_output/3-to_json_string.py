#!/usr/bin/python3
"""Appends a string at the end of a text file"""


import json


def to_json_string(my_obj):
    """
    Converts an object (string) into its JSON representation.

    Args:
    my_obj: The object to be converted to JSON.

    Returns:
    str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
