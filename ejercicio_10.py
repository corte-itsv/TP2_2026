def tabla_multiplicar(numero):
    tabla = []

    for i in range(1, 11):
        tabla.append((i, numero * i))

    return tabla


def mostrar_tabla(tabla, numero):
    print(f"=== Tabla del {numero} ===")
    for multiplicador, resultado in tabla:
        pgirint(f"{numero} x {multiplicador} = {resultado}")


numero = 7
tabla = tabla_multiplicar(numero)
mostrar_tabla(tabla, numero)