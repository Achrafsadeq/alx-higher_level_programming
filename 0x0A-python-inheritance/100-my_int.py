#!/usr/bin/python3
"""100-my_int.py
Defines the MyInt class.
"""


class MyInt(int):
    """Class that inverts the behavior of __eq__ and __ne__."""

    def __eq__(self, other):
        """Overridden to behave like not equal."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Overridden to behave like equal."""
        return super().__eq__(other)
