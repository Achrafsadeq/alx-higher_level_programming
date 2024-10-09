#!/usr/bin/python3
"""Defines a function for multiplying two matrices."""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices and returns the resulting matrix.

    Args:
        m_a (list of lists): The first matrix, where each sublist
        represents a row.
        m_b (list of lists): The second matrix, where each sublist
        represents a row.

    Returns:
        list of lists: A new matrix that is the product of m_a and m_b.

    Raises:
        TypeError: If m_a or m_b are not lists, or if they are not lists
        of lists.
        ValueError: If m_a or m_b are empty matrices.
        TypeError: If any element in m_a or m_b is not an integer or
        float.
        TypeError: If m_a or m_b are not rectangular (i.e., rows have
        varying sizes).
        ValueError: If m_a and m_b cannot be multiplied due to
        incompatible dimensions.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    m_a_empty = False
    m_b_empty = False
    m_a_notrect = False
    m_b_notrect = False
    m_a_notnum = False
    m_b_notnum = False

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if len(row) != len(m_a[0]):
            m_a_notrect = True
        for num in row:
            if not isinstance(num, (int, float)):
                m_a_notnum = True

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if len(row) != len(m_b[0]):
            m_b_notrect = True
        for num in row:
            if not isinstance(num, (int, float)):
                m_b_notnum = True

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    if m_a_notnum:
        raise TypeError("m_a should contain only integers or floats")

    if m_b_notnum:
        raise TypeError("m_b should contain only integers or floats")

    if m_a_notrect:
        raise TypeError("each row of m_a must should be of the same size")

    if m_b_notrect:
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    res = [[] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            c = 0
            for k in range(len(m_b)):
                c += m_a[i][k] * m_b[k][j]
            res[i].append(c)

    return res


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
