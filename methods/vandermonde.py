import numpy as np          # Para cálculos numéricos y álgebra lineal
import sympy as sp          # Para manipulación simbólica de expresiones matemáticas

# Función de interpolación por el método de Vandermonde
def vandermonde(x, y, decimals, x_sym=sp.symbols('x')):
    # Creamos la matriz de Vandermonde: cada fila es [x_i^n, x_i^{n-1}, ..., x_i^0]
    A = np.vander(x, increasing=False)

    # Resolvemos el sistema lineal A·coeffs = y para obtener los coeficientes del polinomio
    coeffs = np.linalg.solve(A, y)

    # Redondeamos los coeficientes a la cantidad de decimales indicada
    rounded_coefficients = np.round(coeffs, decimals)

    # Inicializamos los polinomios simbólicos
    poly = 0
    poly_rounded = 0

    # Construimos los polinomios simbólicos con y sin redondeo
    degree = len(coeffs) - 1  # Grado del polinomio
    for i, coeff in enumerate(coeffs):
        poly += coeff * x_sym**(degree - i)  # Polinomio exacto
        poly_rounded += rounded_coefficients[i] * x_sym**(degree - i)  # Polinomio redondeado

    # Retornamos los coeficientes numéricos y las expresiones simbólicas
    return coeffs, rounded_coefficients, poly, poly_rounded
