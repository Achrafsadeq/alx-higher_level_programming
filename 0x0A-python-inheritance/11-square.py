#!/usr/bin/python3
"""11-square.py
Defines the Square class.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a Square, subclass of Rectangle."""

    def __init__(self, size):
        """Initializes a Square object.

        Args:
            size (int): The size of one side of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns a formatted string for the Square instance."""
        return '[Square] {:d}/{:d}'.format(self.__size, self.__size)
