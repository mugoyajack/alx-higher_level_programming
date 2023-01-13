#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return (list(map(lambda x: [i**2 for i in x], matrix)))
