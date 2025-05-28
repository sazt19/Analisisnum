import pandas as pd
import sympy as sp
import numpy as np
from .sustituacion_b_f import back_substitution

def gauss_total_pivot(A, b):
    A = A.copy().astype(float) #copiamos A y nos aseguramos de que sea de tipo float
    n = len(A)
    i = 0

    old_x = np.arange(n) #este arreglo sirve para llevar el orden original de las variables
    while i < n:
        max_element = 0  # Inicializamos el mayor elemento con 0

        # Buscar el mayor valor absoluto en la submatriz A[i:, i:]
        for row in range(i, n):
            for col in range(i, n):
                if abs(A[row][col]) > abs(max_element):
                    max_element = A[row][col]
                    row_index = row
                    col_index = col

        # Verificamos si se encontró un pivote válido (es decir, distinto de 0)
        if max_element == 0:
            return {"status":"error", "message":"La matriz es singular."}

        # Intercambiar filas: i <-> row_index
        swap_row = A[i].copy()
        A[i] = A[row_index]
        A[row_index] = swap_row

        # También intercambiamos el vector b en la misma posición
        swap_b = b[i].copy()
        b[i] = b[row_index]
        b[row_index] = swap_b

        # Intercambiar columnas: i <-> col_index en la matriz A
        swap_col = A[:, i].copy()
        A[:, i] = A[:, col_index]
        A[:, col_index] = swap_col

        # Registrar el cambio de posición de las variables
        swap_x = old_x[i]
        old_x[i] = old_x[col_index]
        old_x[col_index] = swap_x

        # Realizar la eliminación hacia abajo
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            A[j] = A[j] - factor * A[i]
            b[j] = b[j] - factor * b[i]
            A[j][i] = 0  # Asegurar que el valor sea exactamente cero

        i += 1  # Pasar a la siguiente fila

    # Resolver el sistema triangular superior con sustitución hacia atrás
    x = back_substitution(A, b)

    # Reconstruir el vector solución en el orden original
    new_x = np.zeros(n)
    for i in range(n):
        new_x[old_x[i]] = x[i]

    # Retornar la matriz triangular, el nuevo vector b, y la solución ordenada correctamente
    return {"status":"success", "A":A, "b":b, "x":new_x}