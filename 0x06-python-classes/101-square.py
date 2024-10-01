#!/usr/bin/python3
"""Module containing a Square class."""


class Square:
    """Defines a square object."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a square instance.

        Args:
            size (int): Size of the square (default 0).
            position (tuple): Coordinates of the square's position.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve or update the square size."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve or update the square position."""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the square's area."""
        return self.__size ** 2

    def my_print(self):
        """Display the square using the # character."""
        if self.__size == 0:
            print()
            return

        print("\n" * self.__position[1], end="")
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """String representation of the square."""
        if self.__size == 0:
            return ""
        output = "\n" * self.__position[1]
        for i in range(self.__size):
            output += " " * self.__position[0] + "#" * self.__size + "\n"
        return output.rstrip()
