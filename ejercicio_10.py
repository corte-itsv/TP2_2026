def tabla_multiplicar(numero):    
    tabla = []
    for i in range(1, 11):
        resultado = numero * i
        tabla.append((i, resultado))
    return tabla

def mostrar_tabla(tabla, numero):
    print(f"=== Tabla del {numero} ===")
    for i, resultado in tabla:
        print(f"{numero} x {i} = {resultado}")

numero = 7
tabla = tabla_multiplicar(numero)
mostrar_tabla(tabla, numero)