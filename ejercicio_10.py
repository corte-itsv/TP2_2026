def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
    return f"{numero} x {i} = {resultado}"

def mostrar_tabla(tabla, numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {tabla[i-1]}")


numero = 7
tabla = [numero * i for i in range(1, 11)]
mostrar_tabla(tabla, numero)
tabla_multiplicar(7)
