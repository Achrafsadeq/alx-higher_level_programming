#!/usr/bin/python3
"""
This module defines the Student class, which represents a student
and provides functionality to retrieve its dictionary representation.
"""


class Student:
    """A class that represents a student with attributes for first name,
       last name, and age."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance with the given first name,
        last name, and age.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary representation of the Student instance.

        This dictionary can be used for JSON serialization
        of the student's data.
        """
        return self.__dict__
