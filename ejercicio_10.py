def tabla_multiplicar(numero):
    tabla = []
    for i in range(1, 11):
        tabla.append((i, numero * i))
    return tabla

def mostrar_tabla(tabla, numero):
    print("=== Tabla del", numero, "===")
    for i, resultado in tabla:
        
        print(numero, "x", i, "=", resultado)

numero = 7
t = tabla_multiplicar(numero)
mostrar_tabla(t, numero)