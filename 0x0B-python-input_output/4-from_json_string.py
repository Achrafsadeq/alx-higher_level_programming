#!/usr/bin/python3
"""
This module provides functionality for converting JSON strings
to Python objects.

It contains a single function, `from_json_string`, which takes a JSON-formatted
string and returns the equivalent Python data structure.
"""


import json


def from_json_string(my_str):
    """Returns the Python object representation of a JSON string"""
    return json.loads(my_str)
