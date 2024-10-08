#!/usr/bin/python3
class LockedClass:
    """
    A class that only allows 'first_name' as an instance attribute.
    """
    __slots__ = ['first_name']
