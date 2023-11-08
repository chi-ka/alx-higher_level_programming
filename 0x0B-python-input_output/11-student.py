#!/usr/bin/python3
"""Parses a JSON string and returns the corresponding Python data structure."""


class Student:
    """
    A class to represent a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Args:
            attrs (list of str, optional): A list of attribute names to re
                If None, all attributes are retrieved.

        Returns:
            dict: A dictionary containing the specified attributes of the stu.
        """
        if attrs is None:
            return self.__dict__
        else:
            result_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result_dict[attr] = getattr(self, attr)
            return result_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance using the.

        Args:
            json (dict): A dictionary containing attribute nam.
        """
        for key, value in json.items():
            setattr(self, key, value)
