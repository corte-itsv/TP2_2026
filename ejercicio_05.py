def filtrar_pares(numeros):
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

lista_numeros = [1,2,3,4,5,6,7,8,9,10,11,12]

numeros_pares = filtrar_pares(lista_numeros)

print(numeros_pares)