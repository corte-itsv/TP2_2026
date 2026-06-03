def filtrar_pares(numeros):
    numeros_pares = []
    for n in numeros:
        if n % 2 == 0:
            numeros_pares.append(n)
    return numeros_pares


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


numeros_pares = filtrar_pares(numeros)

print("Versión A:", numeros_pares)
print("Versión B:", numeros_pares)