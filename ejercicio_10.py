def tabla_multiplicar(numero):
    tabla = []

    for multiplicador in range(1, 11):
        tabla.append((multiplicador, numero * multiplicador))

    return tabla


def mostrar_tabla(tabla, numero):
    for multiplicador, resultado in tabla:
        print(f"{numero} x {multiplicador} = {resultado}")

print("=== Tabla del 7 ===")
numero = 7
tabla = tabla_multiplicar(numero)

mostrar_tabla(numero, tabla)