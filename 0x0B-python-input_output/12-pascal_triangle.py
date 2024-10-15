#!/usr/bin/python3
"""
This module defines a function that generates Pascal's Triangle
of a given size.
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle of size n.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        list of lists: A list of lists, where each inner list represents
        a row of Pascal's Triangle. Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
