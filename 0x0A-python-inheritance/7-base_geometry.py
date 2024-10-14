#!/usr/bin/python3
"""Defines the BaseGeometry class derived from 6-base_geometry.py."""


class BaseGeometry:
    """Represents a BaseGeometry entity."""

    def area(self):
        """Computes the area.

        Raises:
            Exception: If the method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Ensures value is a valid integer.

        Args:
            name (str): The name associated with the value.
            value (int): The number being validated.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the value is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
