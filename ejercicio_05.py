def filtrar_pares(numeros):
    numeros_pares = []
    for numero in numeros:
        if numero % 2 == 0:
            numeros_pares.append(numero)
            
    return numeros_pares

    
numeros_benja = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

todos_los_numeros_pares = filtrar_pares(numeros_benja)
print("Numeros pares: ", todos_los_numeros_pares)