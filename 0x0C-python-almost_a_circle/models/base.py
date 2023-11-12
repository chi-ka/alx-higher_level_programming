#!/usr/bin/python3
"""Class Base will be the “base” of all other classes in this project"""


class Base:
    """This is the base of all other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialiizng Class Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
