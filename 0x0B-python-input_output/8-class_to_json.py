#!/usr/bin/python3
"""
  This module provides a function that converts a Python object
  to its corresponding JSON-serializable dictionary representation.

"""


def class_to_json(obj):
    """
       Returns the dictionary description of an object (its attributes)
       for JSON serialization of simple data structures.
    """
    return obj.__dict__
