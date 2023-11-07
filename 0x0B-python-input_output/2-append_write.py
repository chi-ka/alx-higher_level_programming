#!/usr/bin/python3
"""Appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file and returns.

    If the file doesn't exist, it will be created.

    Args:
    filename (str): The name of the file to append to.
    text (str): The text to append to the file.

    Returns:
    int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        characters_added = file.write(text)
    return characters_added
