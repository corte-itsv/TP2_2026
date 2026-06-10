def tabla_multiplicar(numero):
    return [(i, numero * i) for i in range(1, 11)]


def mostrar_tabla(tabla, numero):
    print("=" * 30)
    print(f"Tabla del {numero}")
    print("=" * 30)
    for factor, resultado in tabla:
        print(f"{numero} x {factor} = {resultado}")
    print("=" * 30)

numero = 7
tabla = tabla_multiplicar(numero)


mostrar_tabla(tabla, numero)
tabla_multiplicar(7)
