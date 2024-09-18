#!/usr/bin/python3
def best_score(a_dictionary):
    """Find and return the key with the highest integer value."""
    if not a_dictionary:
        return None

    highest_key = None
    highest_value = float('-inf')

    for key in a_dictionary:
        if a_dictionary[key] > highest_value:
            highest_value = a_dictionary[key]
            highest_key = key

    return highest_key
