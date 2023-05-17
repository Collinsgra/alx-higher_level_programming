#!/usr/bin/python3

def square_matrix_map(matrix=None):
    if matrix is None:
        matrix = []
    return list(map((lambda div: list(map((lambda x: x * x), div))), matrix))
