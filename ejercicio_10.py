def tabla_multiplicar(numero):
    tabla = []

    for i in range(1, 11):
        resultado = numero * i
        tabla.append((i, resultado))

    return tabla


def mostrar_tabla(tabla, numero):
    print("Tabla del", numero)

    for multiplicador, resultado in tabla:
        print(f"{numero} x {multiplicador} = {resultado}")


# Número de prueba
numero = 7

# Generar tabla
tabla = tabla_multiplicar(numero)

# Mostrar tabla
mostrar_tabla(tabla, numero)