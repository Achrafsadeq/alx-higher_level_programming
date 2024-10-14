#!/usr/bin/python3
"""Module that defines a Rectangle class inheriting from BaseGeometry."""

from base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """A class that represents a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """Return a string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
