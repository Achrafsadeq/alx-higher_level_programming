#!/usr/bin/python3

"""Defines a class Square with size validation."""


class Square:
    """A class that defines a square with a private size attribute and validation."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
