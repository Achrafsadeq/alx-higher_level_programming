#!/usr/bin/python3
"""Module that contains the MyList class"""


class MyList(list):
    """A class that inherits from list"""

    def print_sorted(self):
        """Prints the list, but sorted in ascending order"""
        print(sorted(self))
