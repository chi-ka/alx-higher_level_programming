#!/usr/bin/python3
"""A function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """
    Read a text file in UTF-8 encoding and print its contents to stdout.

    Parameters:
    filename (str): The name of the file to be read.

    Note:
    - This function assumes that the file exists and has the necessary permissions.
    - It reads the file line by line and prints each line to the standard output.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
