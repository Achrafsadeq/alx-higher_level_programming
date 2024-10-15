#!/usr/bin/python3
"""
This module provides functionality for saving Python objects to JSON files.

It contains a single function, `save_to_json_file`, which takes a Python object
and a filename, then writes the JSON representation
of the object to the specified file.
"""

import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON format"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
