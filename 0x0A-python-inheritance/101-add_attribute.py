#!/usr/bin/python3
"""101-add_attribute.py
Defines a function to add an attribute to an object.
"""


def add_attribute(obj, name, value):
    """Assigns a new attribute to an object.

    Args:
        obj: The object to which the attribute is added.
        name (str): The name of the attribute.
        value: The value to be assigned to the attribute.

    Raises:
        TypeError: If the object doesn't allow new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
