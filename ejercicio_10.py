def tabla_multiplicar(numero):
    lista_tabla = []
    for multiplicador in range(1,11):
        resultado=numero*multiplicador
        lista_tabla.append((multiplicador, resultado))
    return lista_tabla


def mostrar_tabla(tabla, numero):
    print(f"=== Tabla del{numero} ===")
    for multiplicador, resultado in tabla:
        print(f"{numero}x{multiplicador}={resultado}")


numero = 7
tabla=tabla_multiplicar(numero)
mostrar_tabla(tabla, numero)
        
