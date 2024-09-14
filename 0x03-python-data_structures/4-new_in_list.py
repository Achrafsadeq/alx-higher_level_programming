#!/usr/bin/python3
def new_in_list(my_list, position, element):
    copy = my_list[:]
    if 0 <= position < len(my_list):
        copy[position] = element
    return copy
