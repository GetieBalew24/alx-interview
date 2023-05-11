#!/usr/bin/python3
"""
n x n 2D matrix to rotate it 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Args:
        matrix (list): 2d square matrix
    Return:
        None
    """
    length = len(matrix)
    for k in range(length):
        for l in range(k):
            temporary = matrix[k][l]
            matrix[k][l] = matrix[l][k]
            matrix[l][k] = temporary

    for m in range(length):
        for n in range(int(length / 2)):
            temporary = matrix[m][n]
            matrix[m][n] = matrix[m][length-1-n]
            matrix[m][length-1-n] = temporary