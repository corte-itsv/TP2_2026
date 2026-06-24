def tabla_multiplicar(numero):
    resultado = numero
    lista_de_tuplas = []
    for i in range(1, 11):
        resultado = numero * i
        tupla = (i, resultado)
        lista_de_tuplas.append(tupla)
    return lista_de_tuplas

def mostrar_tabla(tabla, numero):
    for tupla in tabla:
        multiplicador, resultado = tupla
        print(numero," x ",multiplicador," = ", resultado)
    
    


numero = 7


print("=== TABLA DEL 7 ===")
tabla_multiplicada = tabla_multiplicar(numero)
mostrar_tabla(tabla_multiplicada, 7)

