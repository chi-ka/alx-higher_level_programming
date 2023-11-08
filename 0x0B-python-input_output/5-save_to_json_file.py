#!/usr/bin/python3
"""Parses a JSON string and returns the corresponding Python data structure."""


import json


def save_to_json_file(my_obj, filename):
    """
    Parses a JSON string and returns the corresponding Python data structure.

    Args:
    my_str (str): The JSON string to be parsed.

    Returns:
    object: The Python data structure represented by the JSON string.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
