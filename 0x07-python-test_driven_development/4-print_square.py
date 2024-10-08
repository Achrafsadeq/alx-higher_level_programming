#!/usr/bin/python3
"""
This module defines the `print_square` function, which prints a square
using the `#` character.
"""


def print_square(size):
    """
    Prints a square using the `#` character with sides of length `size`.

    Args:
        size (int): The length of each side of the square.

    Raises:
        TypeError: If `size` is not an integer.
        ValueError: If `size` is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size + "\n") * size), end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
