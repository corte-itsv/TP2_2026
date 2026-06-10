def tabla_multiplicar(numero):
    return [(i, numero * i) for i in range(1, 11)]

def mostrar_tabla(tabla, numero):
    print(f"{"=" * 3} Tabla del {numero} { "=" * 3}")
    for factor, resultado in tabla:
        print(f"{numero} x {factor} = {resultado}")
    


def mostrar_tabla(tabla, numero):
   
    print(f"{"=" * 3} Tabla del {numero} {"=" * 3}")
   
    for factor, resultado in tabla:
        print(f"{numero} x{factor:^6}={resultado:^9}")
    


numero = 7
tabla = tabla_multiplicar(numero)


mostrar_tabla(tabla, numero)
tabla_multiplicar(7)
