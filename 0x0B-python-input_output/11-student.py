#!/usr/bin/python3
"""
This module defines the Student class and provides methods
for handling student data, including converting it to and
updating it from a dictionary.
"""


class Student:
    """Represents a student with a first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance with the provided attributes.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        If `attrs` is a list of strings, only those attributes listed
        will be included.

        Args:
            attrs (list, optional): A list of attribute names to include
            in the dictionary.

        Returns:
            dict: A dictionary representation of the Student.
        """
        if attrs is not None:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance using a dictionary.

        Args:
            json (dict): A dictionary containing new attribute values
            to update.
        """
        for k, v in json.items():
            setattr(self, k, v)
