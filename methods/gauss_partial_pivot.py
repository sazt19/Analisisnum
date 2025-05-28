import numpy as np
from methods.sustituacion_b_f import back_substitution

def gauss_partial_pivot(A, b):
    n = len(A) #número de filas de la matriz
    i = 0 #fila actual del proceso de eliminación
    while i < n:
        #encontrar el índice del elemento con el valor absoluto máximo en la columna i
        swap_index = np.argmax(np.abs(A[i:, i])) + i

        #si el valor maximo es cero, la matriz es singular
        if A[swap_index][i] == 0:
            return {"status":"error", "message":"The matrix is singular."}

        #intercambio de filas en A
        swap_row = A[i].copy()
        A[i] = A[swap_index]
        A[swap_index] = swap_row

        #intercambio de filas en b
        swap_b = b[i].copy()
        b[i] = b[swap_index]
        b[swap_index] = swap_b

        #eliminación para hacer ceros debajo del pivote
        for j in range(i+1, n):
            factor = A[j][i] /A[i][i]
            A[j] = A[j] - factor * A[i]
            b[j] = b[j] - factor * b[i]
            A[j][i] = 0
        i += 1 #pasamos a la siguiente fila
    return {"status":"success", "A":A, "b":b}
