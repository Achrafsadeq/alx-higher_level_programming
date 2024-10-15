#!/usr/bin/python3
"""
This module provides functionality for appending text to files.

It contains a single function, `append_write`, which allows
users to add content to the end of an existing file or create
a new file if it doesn't exist.
"""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
