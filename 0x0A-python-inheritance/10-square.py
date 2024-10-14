#!/usr/bin/python3
"""Defines the Square class, inheriting from 9-rectangle.py.

Attributes:
    width (int): Represents the width of the rectangle.
    height (int): Represents the height of the rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a Square, which is a type of Rectangle.

    Args:
        Rectangle (Rectangle): Inherits from the Rectangle class.
    """

    def __init__(self, size):
        """Initializes a Square instance.

        Args:
            size (int): The length of one side of the square.
        """
        # Validates that size is a positive integer
        self.integer_validator("size", size)
        self.__size = size

        # Calls the parent class constructor with equal width and height
        super().__init__(size, size)

    def area(self):
        """Computes the area of the square.

        Returns:
            int: The calculated area (size squared).
        """
        return self.__size ** 2
