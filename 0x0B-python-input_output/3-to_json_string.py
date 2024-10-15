#!/usr/bin/python3
"""
This module provides functionality for converting Python objects
to JSON strings.

It contains a single function, `to_json_string`, which takes a Python object
and returns its JSON representation as a string.
"""

import json


def to_json_string(my_obj):
    """Returns the JSON representation of a string object"""
    return json.dumps(my_obj)
