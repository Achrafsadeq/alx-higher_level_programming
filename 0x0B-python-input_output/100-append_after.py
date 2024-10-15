#!/usr/bin/python3
"""
This module defines a function that inserts a line of text into a file
after each line that contains a specific search string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts `new_string` after each line in the file `filename`
    that contains the `search_string`.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for within each line.
        new_string (str): The string to insert after lines containing
        `search_string`.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
