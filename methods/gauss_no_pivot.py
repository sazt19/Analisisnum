import pandas as pd
import sympy as sp
import numpy as np

from methods.sustituacion_b_f import back_substitution

def gauss_no_pivot(A, b):
    n = len(A)
    i = 0

    while i < n:
        current_value = A[i][i]
        test_value = current_value
        j = i + 1
        swaps = False
        while j < n and test_value == 0:
            swaps = True
            test_value = A[j][i]
            j += 1
        if test_value == 0:
            return {"status":"error", "message":"The matrix is singular."}
        elif swaps:
            j -= 1
            swap_row = A[i].copy()
            A[i] = A[j]
            A[j] = swap_row

            swap_b = b[i].copy()
            b[i] = b[j]
            b[j] = swap_b

        for j in range(i+1, n):
            factor = A[j][i] /A[i][i]
            A[j] = A[j] - factor * A[i]
            b[j] = b[j] - factor * b[i]
            A[j][i] = 0
        i += 1

    return {"status":"success", "A":A, "b":b}

def back_substitution(A,b):
    n = len(A)
    x = np.zeros(n)

    for i in range(n-1, -1, -1):

        x[i] = b[i]
        for j in range(i+1, n):
            if j != i:
                x[i] -= A[i][j] * x[j]
        x[i] = x[i] / A[i][i]
    return x

def forward_substitution(A,b):
    n = len(A)
    x = np.zeros(n)

    for i in range(0,n):
        x[i] = b[i]
        for j in range(i+1, n):
            if j != i:
                x[i] -= A[i][j] * x[j]
        x[i] = x[i] / A[i][i]
    return x
