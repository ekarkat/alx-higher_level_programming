"""function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Check type of matrix"""
    type_error = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(type_error)
    if len(matrix) == 0:
        raise TypeError(type_error)
    for line in matrix:
        if type(line) is not list:
            raise TypeError(type_error)

    """check if each element of mattrix is an int"""
    for line in matrix:
        if type(line) is not list or len(line) == 0:
            raise TypeError(type_error)
    for line in matrix:
        for n in line:
            if type(n) is not int and type(n) is not float:
                raise TypeError(type_error)

    """Check that each list of matrix has the same size"""
    size_line = len(matrix[0])
    for i in range(len(matrix)):
        if len(matrix[i]) != size_line:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    matr = []
    for line in matrix:
        lin = []
        for n in line:
            lin.append(round(n / div, 2))
        matr.append(lin)
    return matr
