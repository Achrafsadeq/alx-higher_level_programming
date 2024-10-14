#!/usr/bin/python3
"""Module that defines a Rectangle class inheriting from BaseGeometry."""

from base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """A class that represents a rectangle.

    This class inherits from BaseGeometry and validates width and height
    as positive integers.
    """

    def __init__(self, width, height):
        """Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is not positive.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
