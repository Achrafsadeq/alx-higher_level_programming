#!/usr/bin/python3
"""This module defines a class Square that represents a square."""

class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square object.

        Args:
            size (int): The size of the square (must be >= 0).
            position (tuple): A tuple of 2 positive integers definin.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): A tuple of 2 positive integers defining.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the # character.

        The square is printed with its position offset, represented by
        spaces before and new lines above, if specified.
        """
        if self.__size == 0:
            print("")
            return

        [print("") for _ in range(0, self.__position[1])]
        for _ in range(0, self.__size):
            [print(" ", end="") for _ in range(0, self.__position[0])]
            [print("#", end="") for _ in range(0, self.__size)]
            print("")

    def __str__(self):
        """Return a string representation of the square.

        This will allow the use of print() to visualize the square with the
        appropriate formatting, taking into account its position and size.
        """
        if self.__size == 0:
            return ""

        square_str = "\n" * self.__position[1]
        for i in range(self.__size):
            square_str += " " * self.__position[0] + "#" * self.__size
            if i != self.__size - 1:
                square_str += "\n"
        return square_str

