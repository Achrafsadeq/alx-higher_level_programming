#!/usr/bin/python3
import sys

if __name__ == "__main__":
    import hidden_4

    # Retrieve all names defined in the hidden_4 module
    defined_names = dir(hidden_4)
    
    # Print each name that does not start with '__' in alphabetical order
    for name in sorted(defined_names):
        if not name.startswith("__"):
            print(name)
