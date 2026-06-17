def tabla_multiplicar(numero):
    resultados = []
    for i in range(1, 11):
        resultado = numero * i
        resultados.append((i, resultado))
    return resultados 

def mostrar_tabla(tabla, numero):
    TablaFinal = []
    for multiplicador, resultado in tabla:
       print(numero, "x", multiplicador, "=", resultado)
tabla = tabla_multiplicar(7)
mostrar_tabla(tabla, 7)