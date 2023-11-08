#!/usr/bin/python3
"""Parses a JSON string and returns the corresponding structure."""


def append_after(filename="", search_string="", new_string=""):
    """Parses a JSON string and returns the corresponding Python ructure."""
    with open(filename, 'r') as input_file, open("temp_file", 'w') as output:
        for line in input_file:
            output.write(line)
            if search_string in line:
                output.write(new_string)

    import os
    os.rename("temp_file", filename)
