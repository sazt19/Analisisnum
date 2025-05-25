import pandas as pd
import sympy as sp
import numpy as np
from .sustituacion_b_f import back_substitution

def gauss_total_pivot(A, b):
    A = A.copy().astype(float)
    n = len(A)
    i = 0

    old_x = np.arange(n)
    while i < n:

        max_element = 0
        for row in range(i, n):
            for col in range(i, n):
                if abs(A[row][col]) > abs(max_element):
                    max_element = A[row][col]
                    row_index = row
                    col_index = col

        #revisar si es valido
        if max_element == 0:
            return {"status":"error", "message":"The matrix is singular."}

        swap_row = A[i].copy()
        A[i] = A[row_index]
        A[row_index] = swap_row

        swap_b = b[i].copy()
        b[i] = b[row_index]
        b[row_index] = swap_b

        # Swap the columns in A
        swap_col = A[:, i].copy()
        A[:, i] = A[:, col_index]
        A[:, col_index] = swap_col

        # Swap the columns in x
        swap_x = old_x[i]
        old_x[i] = old_x[col_index]
        old_x[col_index] = swap_x

        for j in range(i+1, n):
            factor = A[j][i] /A[i][i]
            A[j] = A[j] - factor * A[i]
            b[j] = b[j] - factor * b[i]
            A[j][i] = 0
        i += 1

    x = back_substitution(A, b)
    new_x = np.zeros(n)
    for i in range(n):
        new_x[old_x[i]] = x[i]

    return {"status":"success", "A":A, "b":b, "x":new_x}
