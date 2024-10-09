#!/usr/bin/python3
"""
This module multiplies two matrices using the NumPy library.
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two given matrices.

    Args:
        m_a (array-like): The first input matrix.
        m_b (array-like): The second input matrix.

    Returns:
        ndarray: The product of m_a and m_b.
    """
    return numpy.matmul(m_a, m_b)
