import numpy as np  # Librería para cálculos numéricos y manejo de matrices

# Importamos las funciones de sustitución hacia adelante y hacia atrás
from .sustituacion_b_f import back_substitution, forward_substitution

# Función para realizar la factorización LU (sin pivoteo)
def LU_factorization(A):
    A = A.copy().astype(float)  # Copiamos la matriz A y la convertimos a tipo float
    n = len(A)                  # Número de filas/columnas de la matriz cuadrada
    i = 0                       # Índice de la fila actual

    L = np.eye(n)  # Inicializamos la matriz L como la identidad (triangular inferior)

    # Ciclo principal de la eliminación gaussiana para construir L y U
    while i < n:
        current_value = A[i][i]  # Pivote actual

        # Si el pivote es cero, no se puede continuar sin hacer permutación de filas
        if current_value == 0:
            return {
                "status": "error",
                "message": "La matriz no se puede descomponer sin permutar filas o es singular."
            }

        # Eliminación hacia abajo y construcción de L
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]      # Calculamos el multiplicador (factor)
            A[j] = A[j] - factor * A[i]     # Restamos la fila pivote multiplicada por el factor
            A[j][i] = 0                     # Forzamos el valor a cero por estabilidad numérica
            L[j][i] = factor                # Guardamos el factor en la matriz L

        i += 1  # Avanzamos al siguiente pivote

    # Retornamos éxito junto con las matrices L y U (U es A transformada)
    return {
        "status": "success",
        "U": A,   # Matriz triangular superior resultante
        "L": L    # Matriz triangular inferior
    }

# Función para resolver un sistema Ax = b usando L y U
def solve_LU(L, U, b):
    y = forward_substitution(L, b)  # Resolvemos Ly = b
    x = back_substitution(U, y)     # Resolvemos Ux = y
    return x                        # Devolvemos la solución final x
