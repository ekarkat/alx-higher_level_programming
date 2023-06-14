#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    new_matrix = []
    for line in matrix:
        new_matrix.append(list(map(lambda x: x**2, line)))
    return (new_matrix)
