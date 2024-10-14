#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BaseGeometry:
    """A class representing base geometry"""

    def area(self):
        """
        Calculates the area of the geometry.

        Raises:
            Exception: Always raises an Exception with the message
                       "area() is not implemented"
        """
        raise Exception("area() is not implemented")
