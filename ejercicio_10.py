def tabla_multiplicar(numero):
    lista_multi_resul = []
    for i in range(1, 11):
        multiplicador = i
        resltado = i * numero
        tupla = (multiplicador, resltado)
        lista_multi_resul.append(tupla)
    return lista_multi_resul


def mostrar_tabla(lista, numero):
    for par_multi_resul in lista:
        multiplicador, resultado = par_multi_resul
        print(numero, "x", multiplicador, "=", resultado)
    return 

print("=== TABLA DEL 7 ===")    

lista_multi_resul = tabla_multiplicar(7)
mostrar_tabla(lista_multi_resul, 7)