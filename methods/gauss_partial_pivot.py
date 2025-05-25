import pandas as pd
import sympy as sp
import numpy as np
from methods.sustituacion_b_f import back_substitution

def gauss_partial_pivot(A, b):
    n = len(A)
    i = 0
    while i < n:

        swap_index = np.argmax(np.abs(A[i:, i])) + i
        if A[swap_index][i] == 0:
            return {"status":"error", "message":"The matrix is singular."}

        swap_row = A[i].copy()
        A[i] = A[swap_index]
        A[swap_index] = swap_row

        swap_b = b[i].copy()
        b[i] = b[swap_index]
        b[swap_index] = swap_b

        for j in range(i+1, n):
            factor = A[j][i] /A[i][i]
            A[j] = A[j] - factor * A[i]
            b[j] = b[j] - factor * b[i]
            A[j][i] = 0
        i += 1
    return {"status":"success", "A":A, "b":b}
