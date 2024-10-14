#!/usr/bin/python3
"""9-rectangle.py
Defines a Rectangle class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a Rectangle, subclass of BaseGeometry."""

    def __init__(self, width, height):
        """Initializes the rectangle with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        # Validate that width and height are positive integers
        self.integer_validator('width', width)
        self.integer_validator('height', height)

        # Set the private attributes for width and height
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """Provides a string representation of the rectangle.

        Returns:
            str: The formatted string representing the rectangle.
        """
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
