#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0

    for r in reversed(roman_string):
        num = digits.get(r, 0)
        if num >= prev_value:
            total += num
        else:
            total -= num
        prev_value = num

    return total
