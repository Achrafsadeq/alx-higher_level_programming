#!/usr/bin/python3

"""Module for the Square class that supports comparison operations."""



class Square:
    """Defines a square with size and comparison capabilities."""

    def __init__(self, size=0):
        """
        Initialize a new square with a given size.

        Args:
            size (int or float): The size of the square's side.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve or update the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Compare equality of two squares' areas."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare inequality of two squares' areas."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if one square's area is less than another's."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if one square's area is less than or equal to another's."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if one square's area is greater than another's."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if one square's area is greater than or equal to another's."""
        return self.area() >= other.area()

