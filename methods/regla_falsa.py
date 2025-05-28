import pandas as pd  # Librería para crear y manejar tablas (DataFrames)

def regula_falsi(a, b, niter, tol, tolerance_type, function):
    table = []  # Lista que almacenará cada fila de resultados
    row = {}    # Diccionario para una fila de la tabla

    # Determinamos el tipo de error que se va a calcular
    Error = "Relative Error" if tolerance_type == "Significant Figures" else "Absolute Error"

    # Primer cálculo de intersección (estimación inicial de la raíz)
    row["a"] = a
    row["b"] = b
    row["x_intersect"] = (function(b) * a - function(a) * b) / (function(b) - function(a))  # Fórmula de la Regla Falsa
    row["f(a)"] = function(a)
    row["f(x_intersect)"] = function(row["x_intersect"])
    row["f(b)"] = function(b)
    row[Error] = None  # En la primera iteración no hay error previo
    table.append(row)  # Guardamos la primera fila en la tabla

    err = 100  # Inicializamos el error alto para entrar al bucle

    # Verificamos que la función cambie de signo en el intervalo [a, b]
    if (function(a) * function(b) > 0):
        return {"status": "error", "message": "Argumentos inválidos: la función no cambia de signo en el intervalo."}
    else:
        x_intersect = row["x_intersect"]
        iter = 0

        # Bucle principal: iterar hasta que se cumpla la tolerancia o se alcancen las iteraciones máximas
        while (iter < niter and err > tol):

            # Si encontramos la raíz exacta, terminamos
            if function(a) == 0:
                return table

            # Elegimos el nuevo subintervalo dependiendo del signo de f(a)*f(x_intersect)
            if function(a) * function(x_intersect) < 0:
                b = x_intersect
            else:
                a = x_intersect

            iter += 1  # Aumentamos el contador de iteraciones
            old_intersect = x_intersect

            # Calculamos la nueva intersección
            x_intersect = (function(b) * a - function(a) * b) / (function(b) - function(a))

            # Guardamos los datos de la iteración en una nueva fila
            row = {}
            row["a"] = a
            row["x_intersect"] = x_intersect
            row["b"] = b
            row["f(a)"] = function(a)
            row["f(x_intersect)"] = function(x_intersect)
            row["f(b)"] = function(b)

            # Calculamos el error actual (relativo o absoluto)
            if Error == "Relative Error":
                row[Error] = abs((x_intersect - old_intersect) / x_intersect)
            else:
                row[Error] = abs(x_intersect - old_intersect)

            table.append(row)  # Añadimos la fila a la tabla
            err = row[Error]   # Actualizamos el valor de error

        # Convertimos la lista de diccionarios en un DataFrame para facilitar el análisis
        df = pd.DataFrame(table)
        return {"status": "success", "table": df}
