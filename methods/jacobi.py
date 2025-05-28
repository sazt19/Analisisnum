import numpy as np        # Librería para operaciones matemáticas y matrices
import pandas as pd       # Librería para construir tablas de resultados (DataFrame)

# Función para calcular el error entre dos iteraciones consecutivas
def calculate_error(X, X_L, norm=2, error_type=None):
    diff = np.abs(X - X_L)  # Diferencia absoluta entre la solución nueva y la anterior

    # Cálculo del error según la norma seleccionada
    if norm == 1:  # Norma L1: suma de los valores absolutos
        norm_error = np.sum(diff)
    elif norm == 2:  # Norma L2: distancia euclidiana
        norm_error = np.sqrt(np.sum(diff**2))
    elif norm == 'inf':  # Norma infinito: el valor máximo de la diferencia
        norm_error = np.max(diff)
    else:
        raise ValueError("Valor inválido para la norma. Debe ser 1, 2 o 'inf'.")

    # Si el tipo de error es "cifras significativas", se calcula el error relativo
    if error_type == "Significant Figures":
        relative_error = norm_error / np.abs(X).max()  # Se normaliza por el valor más grande de X
        error = relative_error

    # Si el tipo de error es "decimales correctos", se deja el error absoluto
    elif error_type == "Correct Decimals":
        error = norm_error
    else:
        raise ValueError("Tipo de error inválido. Debe ser 'Significant Figures' o 'Correct Decimals'.")

    return error

# Función para calcular el radio espectral de la matriz de iteración T
def rad_esp(T):
    eig = np.linalg.eigvals(T)         # Se calculan los eigenvalores (valores propios)
    rsp = np.max(np.abs(eig))          # El radio espectral es el valor absoluto máximo
    return rsp

# Función para construir la tabla con las soluciones por iteración
def make_tableMat(x_m_list, errores):
    table = pd.DataFrame(x_m_list[1:], columns=x_m_list[0])  # Crear DataFrame desde la lista de soluciones
    table["Error"] = errores                                  # Añadir columna de errores
    return table

# Método de Jacobi para resolver sistemas lineales Ax = b
def jacobi_method(A, b, X_i, tol, niter, norm=2, error_type="Significant Figures"):
    err = None
    errores = [100]  # Lista para registrar los errores por iteración
    if error_type == "Significant Figures":
        errores = [0]  # Si se usan cifras significativas, comenzamos con error 0

    # Crear etiquetas X_1, X_2, ..., y agregar la solución inicial
    X_val = [list(f"X_{i+1}" for i in range(len(b)))]
    X_val.append(list(map(int, X_i)))  # Convertimos X_i a enteros para mostrar la tabla

    # Verificar que la matriz diagonal (D) sea invertible
    try:
        D = np.diag(np.diagonal(A))    # Extraemos la matriz diagonal de A
        np.linalg.inv(D)               # Intentamos invertir D
    except np.linalg.LinAlgError:
        err = "La matriz A es singular (no invertible). Verifica la matriz e intenta de nuevo."
        return None, None, None, err, None, None

    # Descomposición de A en D (diagonal), L (parte inferior), U (parte superior)
    D = np.diag(np.diagonal(A))
    L = -1 * np.tril(A, -1)  # Parte inferior (sin diagonal), con signo invertido
    U = -1 * np.triu(A, 1)   # Parte superior (sin diagonal), con signo invertido

    # Cálculo de las matrices de iteración T y C para el método de Jacobi
    T = np.linalg.inv(D) @ (L + U)
    C = np.linalg.inv(D) @ b

    # Verificar si la solución inicial ya cumple con la tolerancia
    E = (A @ X_i) - b  # Cálculo del residuo (Ax - b)
    if np.allclose(E, np.zeros(len(b)), atol=tol):
        return X_i, make_tableMat(X_val, errores), rad_esp(T), err, T, C

    # Iteraciones de Jacobi
    X = X_i.copy()  # Inicializamos X con la estimación inicial

    for i in range(1, niter):
        X_L = X.copy()          # Guardamos la solución anterior
        X = T @ X + C           # Aplicamos la fórmula de Jacobi

        X_val.append(np.squeeze(X))  # Añadimos la solución a la tabla

        error = calculate_error(X, X_L, norm, error_type)  # Calculamos el error
        errores.append(error)

        if error < tol:  # Si el error es menor que la tolerancia, detenemos
            return X, make_tableMat(X_val, errores), rad_esp(T), err, T, C

    # Si el método no converge dentro del número de iteraciones
    err = f"El método de Jacobi no convergió después de {niter} iteraciones. Revisa los parámetros del sistema o aumenta el número de iteraciones."

    return X, make_tableMat(X_val, errores), rad_esp(T), err, T, C
