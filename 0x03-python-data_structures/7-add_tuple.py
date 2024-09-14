#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_1 = tuple_a[:2] + (0,) * (2 - len(tuple_a))
    tuple_2 = tuple_b[:2] + (0,) * (2 - len(tuple_b))
    return tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1]
