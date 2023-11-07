#!/usr/bin/python3
"""Parses a JSON string and returns the corresponding Python data structure."""


import sys
from 5-save_to_json_file.py import save_to_json_file
from 6-load_from_json_file.py import load_from_json_file

def add_args_to_list(args):
    """
    Add the command-line arguments to a list and save it as a JSON representation in a file named "add_item.json".

    Args:
        args (list): A list of arguments to be added to the existing list.

    Returns:
        None
    """
    try:
        my_list = load_from_json_file("add_item.json")
    except (FileNotFoundError, json.JSONDecodeError):
        my_list = []

    my_list.extend(args)

    save_to_json_file(my_list, "add_item.json")
