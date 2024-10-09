#!/usr/bin/python3
"""This module defines the add_integer function."""


def add_integer(a, b=98):
    """Adds two numbers, where both must be either integers or floats.

    Args:
        a: The first number, must be an integer or float.
        b: The second number, must be an integer or float (default is 98).

    Raises:
        TypeError: If either a or b is not an integer or float.

    Returns:
        The sum of a and b as integers.
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
