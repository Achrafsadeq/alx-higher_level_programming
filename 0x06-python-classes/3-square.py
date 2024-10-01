#!/usr/bin/python3

"""Defines a class Square with size validation and a method."""



class Square:
    """A class that defines a square with a private size attribute."""

    def __init__(self, size=0):
        """
        Initialize the square with size validation.

        Args:
            size (int, optional): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # Private instance attribute

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

