#!/usr/bin/python3
def square_matrix_simple(matrix=None):
    if matrix is None:
        matrix = []
    return [list(map(lambda x: x ** 2, _div)) for _div in matrix]
