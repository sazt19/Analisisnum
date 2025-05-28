import numpy as np
import pandas as pd

def calculate_error(X, X_L, norm=2, error_type=None):
    #Diferencia absoluta entre las soluciones actuales y las anteriores
    diff = np.abs(X - X_L)

    #Selecciona la norma para calcular el error
    if norm == 1:  # Norma L1: suma de diferencias absolutas
        norm_error = np.sum(diff)
    elif norm == 2:  # Norma L2: distancia euclidiana
        norm_error = np.sqrt(np.sum(diff**2))
    elif norm == 'inf':  # Norma L∞: el mayor valor absoluto de las diferencias
        norm_error = np.max(diff)
    else:
        raise ValueError("Invalid value for error_rel. Must be 1, 2, or 'inf'.")

    #Error relativo si se seleccionan cifras significativas
    if error_type == "Significant Figures":
        relative_error = norm_error / np.abs(X).max()  # Relative to the max value of X
        error = relative_error

    #Error absoluto si se seleccionan decimales correctos
    elif error_type == "Correct Decimals":
        error = norm_error

    else:
        raise ValueError("Invalid value for error_type. Must be 'Significant Figures' or 'Correct Decimals'.")

    return error

# función para calcular el radio espectral de la matriz T
def rad_esp(T):
    eig = np.linalg.eigvals(T)  # Calcula los valores propios
    rsp = np.max(np.abs(eig))  # el radio espectral es el máximo valor absoluto
    return rsp

#función para construir la tabla de iteraciones con errores
def make_tableMat(x_m_list, errores):
    table = pd.DataFrame(x_m_list[1:], columns=x_m_list[0])  # Crea un datagrame con las soluciones
    table["Error"] = errores  # Añade la columna de errores
    return table


def gauss_seidel_method(A, b, X_i, tol, niter, norm=2, error_type="Significant Figures"):
    err = None
    errores = [100]  # Lista para almacenar los errores de cada iteración
    if error_type == "Significant Figures":
        errores = [0] #Si se usa error relativo, iniciamos con 0

    X_val = [list(f"X_{i+1}" for i in range(len(b)))]  # Crea etiquetas para X
    X_val.append(list(map(float, X_i)))  # Añade el vector incial como punto de partida

    #verificamos que la matriz A no sea singular
    try:
        det = np.linalg.det(A)
        if det == 0:
            err = "Matrix A is singular (non-invertible). Please check the matrix and try again."
            return None, None, None, err, None, None
    except np.linalg.LinAlgError:
        err = "Matrix A is singular (non-invertible). Please check the matrix and try again."
        return None, None, None, err, None, None

    # Descomposición de la matriz A en D, L(inferior) y U(superior)
    D = np.diag(np.diagonal(A))
    L = -1 * np.tril(A, -1)
    U = -1 * np.triu(A, 1)

    # Matriz de iteración T y vector de constantes C
    T = np.linalg.inv(D - L) @ U
    C = np.linalg.inv(D - L) @ b

    #Verfica si el valor inicial ya cumple la tolerancia
    E = (A @ X_i) - b  # Residuo de Ax-b
    if np.allclose(E, np.zeros(len(b)), atol=tol):
        return X_i, make_tableMat(X_val, errores), rad_esp(T), err, T, C

    X = X_i.copy()  #Inicializar X con la estimación inicial
    for i in range(1, niter):
        X_L = X.copy()  # Guardar la iteración anterior

        #Actualizar cada componente de X usando la formula de Gauss-Seidel
        for j in range(len(b)):
            X[j] = (b[j] - np.dot(A[j, :j], X[:j]) - np.dot(A[j, j+1:], X_L[j+1:])) / A[j, j]

        #Añadir nueva estimación a la tabla
        X_val.append(np.squeeze(X.copy()))

        # Calcular el error
        error = calculate_error(X, X_L, norm, error_type)
        errores.append(error)

        # Verificar si el error es menor que la tolerancia
        if error < tol:
            return X, make_tableMat(X_val, errores), rad_esp(T), err, T, C

    #Si el método no converge después del número máximo de iteraciones
    err = f"Gauss-Seidel method did not converge after {niter} iterations. Please check system parameters or increase the number of iterations."

    return X, make_tableMat(X_val, errores), rad_esp(T), err, T, C
