#!/usr/bin/python3
"""
This module provides a function to rotate a 2D matrix by 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix by 90 degrees clockwise in place.

    Args:
        matrix (list of list of int): 2D matrix to rotate.

    Returns:
        None: The matrix is modified in place.
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rotate_2d_matrix(matrix)
    print(matrix)
