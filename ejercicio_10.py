def tabla_multiplicar(numero):
    return [(i, numero * i) for i in range(1, 11)]


def mostrar_tabla(tabla, numero):
    print(f"=== Tabla del {numero} ===")
    for multiplicador, resultado in tabla:
        print(f"{numero} x {multiplicador:2} = {resultado:3}")


numero = 7
tabla = tabla_multiplicar(numero)
mostrar_tabla(tabla, numero)