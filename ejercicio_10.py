def tabla_multiplicar(numero):
    return [(i, i * numero) for i in range(1, 11)]

def mostrar_tabla(tabla, numero):
    print(f"=== Tabla del {numero} ===")
    for mult, res in tabla:
        print(f"{numero} x {mult:>2} ={res:>3}")

numero = 7
t = tabla_multiplicar(numero)
mostrar_tabla(t, numero)