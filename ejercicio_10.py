def tabla_multiplicar(numero):
    tabla = []
    for i in range(1, 11):
        tabla.append((i, numero * i))
    return tabla

def mostrar_tabla(tabla, numero):
    print(f"=== Tabla del {numero} ===")
    for multiplicador, resultado in tabla:
        print(f"{numero} x {multiplicador:>2} = {resultado:>3}")

numero_ejemplo = 7
tabla_datos = tabla_multiplicar(numero_ejemplo)
mostrar_tabla(tabla_datos, numero_ejemplo)
