import pandas as pd
import sympy as sp
import numpy as np

def gauss_no_pivot(A, b):
    n = len(A)
    i = 0

    while i < n:
        current_value = A[i][i]
        test_value = current_value
        j = i + 1
        swaps = False
        #verifica si el pivote es cero y busca un elemento no nulo para hacer el intercambio
        while j < n and test_value == 0:
            swaps = True
            test_value = A[j][i]
            j += 1

        #si no se encuentra un elemento no nulo, la matriz es singular
        if test_value == 0:
            return {"status":"error", "message":"The matrix is singular."}

        #si hubo cambio de filas, se hace el intercambio
        elif swaps:
            j -= 1
            swap_row = A[i].copy()
            A[i] = A[j]
            A[j] = swap_row

            swap_b = b[i].copy()
            b[i] = b[j]
            b[j] = swap_b

        #eliminación de elementos debajo del pivote
        for j in range(i+1, n):
            factor = A[j][i] /A[i][i]
            A[j] = A[j] - factor * A[i]
            b[j] = b[j] - factor * b[i]
            A[j][i] = 0
        i += 1

    return {"status":"success", "A":A, "b":b}
