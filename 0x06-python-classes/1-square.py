#!/usr/bin/python3

"""
Module 1-square
Defines a class Square with a private instance attribute size.
"""

class Square:
    """
    A class that defines a square with a private attribute for size.
    """

    def __init__(self, size):
        """
        Initialize the square with a private size attribute.

        Args:
            size (int): The size of the square.
        """
        self.__size = size  # Private instance attribute
