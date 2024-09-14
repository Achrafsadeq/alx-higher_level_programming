#!/usr/bin/python3
def delete_at(my_list=[], index=0):
    if 0 <= index < len(my_list):
        my_list.pop(index)
    return my_list
