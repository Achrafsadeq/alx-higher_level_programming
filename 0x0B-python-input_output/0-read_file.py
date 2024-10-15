#!/usr/bin/python3
"""
This module contains a function that reads a text file and prints its contents.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read.
        Defaults to an empty string.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
