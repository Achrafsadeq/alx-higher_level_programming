#!/usr/bin/python3
""" This script provides a function for writing text to a file."""


def write_file(filename="", text=""):
    """Writes the given string to a UTF-8 encoded text file."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
