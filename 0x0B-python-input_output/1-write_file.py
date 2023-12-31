#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    Write a string to a text file in UTF-8 encoding 
    and return the number of characters written.

    Parameters:
    filename (str): The name of the file to be written.
    text (str): The text to be written to the file.

    Returns:
    int: The number of characters written to the file.

    """
    with open(filename, 'w', encoding='utf-8') as file:
        char_count = file.write(text)
        return char_count
