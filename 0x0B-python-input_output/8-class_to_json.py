#!/usr/bin/python3
"""Parses a JSON string and returns the corresponding Python data structure."""


def class_to_json(obj):
    """Parses a JSON string and Python data structure."""
    if not hasattr(obj, "__dict__"):
        raise TypeError("Object is not serializable")

    result = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            result[key] = value

    return result
