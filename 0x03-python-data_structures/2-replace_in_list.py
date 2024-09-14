#!/usr/bin/python3
def replace_in_list(my_list, position, element):
    if 0 <= position < len(my_list):
        my_list[position] = element
    return my_list
