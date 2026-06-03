def tabla_multiplicar(numero):

    tabla = []
    for i in range(1, 11):
        tabla.append((i, numero * i))
    return tabla

def mostrar_tabla(tabla, numero):

    print(f"=== Tabla del {numero} ===")
    for multiplicador, resultado in tabla:
        print(f"{numero} x {multiplicador:2d} = {resultado:3d}")


num_tabla = 7
mi_tabla = tabla_multiplicar(num_tabla)

mostrar_tabla(mi_tabla, num_tabla)
print()