def tabla_multiplicar(numero):
    lista = []
    for i in range(1, 11):
        lista.append((i, numero * i))
    return lista
 
def mostrar_tabla(tabla, numero):
    print("\n=== Tabla del " + str(numero) + " ===")
    for multiplicador, resultado in tabla:
        print(str(numero) + " x " + str(multiplicador).rjust(2) + " = " + str(resultado).rjust(3))
 
tabla = tabla_multiplicar(7)
mostrar_tabla(tabla, 7)
 