#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_elements = set(my_list)
    total = 0
    for value in unique_elements:
        total += value
    return total
