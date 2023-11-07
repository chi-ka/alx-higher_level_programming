#!/usr/bin/python3
"""Parses a JSON string and returns the corresponding Python data structure."""

import json

def load_from_json_file(filename):
    """
    Load an object from a JSON file and return it.

    Args:
        filename (str): The name of the JSON file from which to load the object.

    Returns:
        object: The deserialized object from the JSON file.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None
