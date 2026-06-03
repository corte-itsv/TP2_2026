def tabla_multiplicar(numero):
    tabla = []
    for i in range(1, 11):
        tabla.append((i, numero * i))
    return tabla
    return [(i, i * numero) for i in range(1, 11)]

def mostrar_tabla(tabla, numero):
    print("=== Tabla del", numero, "===")
    for i, resultado in tabla:
        
        print(numero, "x", i, "=", resultado)
    print(f"=== Tabla del {numero} ===")
    for mult, res in tabla:
        print(f"{numero} x {mult:>2} ={res:>3}")

numero = 7
tabla = tabla_multiplicar(numero)
mostrar_tabla(tabla, numero)