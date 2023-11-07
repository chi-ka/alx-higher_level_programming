#!/usr/bin/python3
"""Parses a JSON string and returns the corresponding Python data structure."""

import json
import sys
import os.path

from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

if __name__ == "__main__":
    filename = "add_item.json"
    my_list = []

    if os.path.exists(filename):
        my_list = load_from_json_file(filename)

    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, filename)
