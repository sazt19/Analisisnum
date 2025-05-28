import pandas as pd
def bisection(a, b, niter, tol, tolerance_type, function):

    #validamos que el intervalo sea correcto
    if b < a:
        return {"status":"error" , "message":"Invalid Arguments, b must be greater than a."}

    table = [] #almacenaremos las filas de los resultados
    row = {} #Diccionariio para una fila
    Error = "Relative Error" if tolerance_type == "Significant Figures" else "Absolute Error"

    # Primer registro antes de iniciar iteraciones
    row["a"] = a
    row["b"] = b
    row["mid"] = (a + b)/2
    row["f(a)"] = function(a)
    row["f(mid)"] = function((a + b)/2)
    row["f(b)"] = function(b)
    row[Error] = None #No hay error en la primera iteración
    table.append(row)
    err = 100

    #validamos que la función cambie de signo en el intervalo
    if (function(a)*function(b) > 0):
        return {"status":"error" , "message":"Invalid Arguments, the function does not change sign in the interval."}
    else:
        mid = (a + b)/2
        iter = 0
        while (iter < niter and err > tol):
            #escogemos el subintervalo donde cambia de signo
            if (function(a)*function(mid) <= 0):
                b = mid
            else:
                a = mid
            iter += 1
            prev_mid = mid
            mid = (a + b)/2 #nuevo punto medio

            row = {} #creamos una nueva fila
            row["a"] = a
            row["b"] = b
            row["mid"] = mid
            row["f(a)"] = function(a)
            row["f(mid)"] = function(mid)
            row["f(b)"] = function(b)

            #calculo del error
            if Error == "Relative Error":
                row[Error] = abs((mid - prev_mid)/mid)
            else:
                row[Error] = abs(mid - prev_mid)

            err = row[Error] #actualizamos el error actual
            table.append(row) #agregamos la fila a la tabla

        #convertimos la tabla a un DataFrame de pandas
        df = pd.DataFrame(table)
        return {"status":"success", "table":df}