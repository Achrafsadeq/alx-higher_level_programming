#!/usr/bin/python3
"""
This module defines the `say_my_name` function, which prints a full name
using the provided first and last name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the full name using the provided `first_name` and `last_name`.

    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print (optional).

    Raises:
        TypeError: If either `first_name` or `last_name` is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
