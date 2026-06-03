def filtrar_pares(numeros):
    lista_pares = []

    for numero in numeros:
        if numero %2 == 0:
            lista_pares.append(numero)
    
    return lista_pares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

resultado = filtrar_pares(numeros)

print(resultado)
