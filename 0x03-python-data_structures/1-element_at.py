#!/usr/bin/python3
def element_at(my_list, position):
    if not (0 <= position < len(my_list)):
        return 'None'
    else:
        return my_list[position]
