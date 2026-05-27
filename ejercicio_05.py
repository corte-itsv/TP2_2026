def filtrar_pares(numeros):
    pares = []
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
    return pares

# Pruebas
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(filtrar_pares(numeros))