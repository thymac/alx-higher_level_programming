#!/usr/bin/python3

"""Defines a matrix division function."""

def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int or float): The divisor.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats.
        TypeError: If the rows of the matrix are not of equal length.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is equal to 0.

    Returns:
        list: A new matrix representing the result of the division.
    """
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(ele / div, 2) for ele in row] for row in matrix]

