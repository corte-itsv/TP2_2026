def tabla_multiplicar(numero):
    tabla = []

    for multiplicador in range(1, 11):
        tabla.append((multiplicador, numero * multiplicador))

    return tabla


def mostrar_tabla(numero, tabla):
    for dato in tabla:
        print(f"{numero} x {dato[0]} = {dato[1]}")

print("=== Tabla del 7 ===")
numero = 7
tabla = tabla_multiplicar(numero)

mostrar_tabla(numero, tabla)