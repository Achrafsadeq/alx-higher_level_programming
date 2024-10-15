#!/usr/bin/python3
"""
This module defines the Student class, which allows for the creation
of student instances and provides functionality to retrieve their
attributes as a dictionary, with optional filtering.
"""


class Student:
    """A class used to represent a student with first name,
       last name, and age."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance with the provided first name,
        last name, and age.

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
        Returns a dictionary representation of the Student instance.
        If `attrs` is a list of strings, only the attributes contained
        in the list are returned.

        Args:
            attrs (list, optional): A list of attribute names to include
            in the dictionary.

        Returns:
            dict: A dictionary containing the student's attributes,
            optionally filtered by `attrs`.
        """
        obj = self.__dict__.copy()
        if type(attrs) is list:
            # Ensure all elements in attrs are strings
            for item in attrs:
                if type(item) is not str:
                    return obj

            filtered_dict = {}
            # Populate filtered_dict with matching attributes
            for attr in attrs:
                if attr in obj:
                    filtered_dict[attr] = obj[attr]
            return filtered_dict

        return obj
