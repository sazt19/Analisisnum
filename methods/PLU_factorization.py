import pandas as pd         # (No se usa aquí, pero podría usarse para generar tablas de resultados)
import sympy as sp          # (Tampoco se utiliza aquí)
import numpy as np          # Librería principal para manipulación numérica

# Importación de funciones para resolver sistemas triangulares
from .sustituacion_b_f import back_substitution, forward_substitution

# Función para realizar la factorización PLU (con pivoteo parcial)
def PLU_factorization(A):
    A = A.copy().astype(float)  # Copiamos A como matriz de números flotantes para evitar errores de tipo
    n = len(A)                  # Número de filas (o columnas) de la matriz cuadrada
    i = 0                       # Fila actual que se está procesando

    L = np.eye(n).astype(float)  # Matriz identidad para L (triangular inferior)
    P = np.eye(n).astype(float)  # Matriz identidad para P (permutaciones)

    # Bucle principal para aplicar eliminación gaussiana con pivoteo parcial
    while i < n:
        P_new = np.eye(n)  # Inicializamos una nueva matriz de permutación
        # Buscamos el índice de la fila con el mayor valor absoluto en la columna actual
        swap_index = np.argmax(np.abs(A[i:, i])) + i

        # Si el pivote es cero, la matriz es singular y no se puede descomponer
        if A[swap_index][i] == 0:
            return {"status": "error", "message": "La matriz no se puede descomponer porque es singular."}

        # Si se necesita intercambiar filas
        if swap_index != i:
            # Intercambiar filas en A
            swap_row = A[i].copy()
            A[i] = A[swap_index]
            A[swap_index] = swap_row

            # Construimos la matriz de permutación P_new para este intercambio
            P_new[i][i] = 0
            P_new[swap_index][swap_index] = 0
            P_new[swap_index][i] = 1
            P_new[i][swap_index] = 1

            # Actualizamos la matriz P acumulada
            P = P_new @ P

        # Eliminación de Gauss: hacemos ceros debajo del pivote
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]       # Calculamos el factor de eliminación
            A[j] = A[j] - factor * A[i]      # Restamos la fila pivote escalada
            A[j][i] = 0                      # Forzamos el valor a cero por precisión
            L[j][i] = factor                 # Guardamos el factor en L

        i += 1  # Pasamos a la siguiente fila

    # Al finalizar, A se convierte en U (triangular superior)
    return {"status": "success", "U": A, "L": L, "P": P}

# Función para resolver el sistema Ax = b usando las matrices P, L, U
def solve_PLU(P, L, U, b):
    y = forward_substitution(L, np.dot(P, b))  # Resolvemos Ly = Pb (aplicamos la permutación)
    x = back_substitution(U, y)               # Resolvemos Ux = y
    return x
