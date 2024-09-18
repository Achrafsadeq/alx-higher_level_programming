#!/usr/bin/python3
def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer."""
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    length = len(roman_string)

    for i in range(length):
        # Get the value of the current Roman numeral
        current_value = roman_dict.get(roman_string[i], 0)

        # If it's not the last numeral and the current one is smaller than the next, subtract
        if i < length - 1 and current_value < roman_dict.get(roman_string[i + 1], 0):
            total -= current_value
        else:
            total += current_value

    return total
