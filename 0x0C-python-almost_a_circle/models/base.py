#!/usr/bin/python3
"""Class Base will be the “base” of all other classes in this project"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []
        filename = f"{cls.__name__}.json"
        json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
    
        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return[]
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)
        else:
            # Handle other classes accordingly
            raise NotImplementedError(f"Class {cls.__name__} not supported in create method.")

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a file."""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                instances = [cls.create(**d) for d in dictionaries]
                return instances
        except FileNotFoundError:
            return []
