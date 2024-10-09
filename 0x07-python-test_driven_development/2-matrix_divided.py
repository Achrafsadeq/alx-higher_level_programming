#!/usr/bin/python3
"""
This module contains the function `matrix_divided` which divides all
elements of a matrix by a given divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides each element in the given matrix by the divisor `div`.

    Args:
        matrix (list): A list of lists containing integers or floats.
        div (int/float): The divisor to divide each element by.

    Returns:
        list: A new matrix (list of lists) with each element divided by `div`.

    Raises:
        TypeError: If `matrix` is not a list of lists of integers/floats,
                   if the rows in `matrix` are not of the same size, or
                   if `div` is not an integer or float.
        ZeroDivisionError: If `div` is zero.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(x / div, 2) for x in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
