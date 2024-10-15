#!/usr/bin/python3
"""
This module provides functionality for loading Python objects from JSON files.

It contains a single function, `load_from_json_file`, which reads a JSON file
and returns its contents as a Python object.
"""

import json


def load_from_json_file(filename):
    """Creates a Python object from a given JSON file"""
    with open(filename) as f:
        return json.load(f)
