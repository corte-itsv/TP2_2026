def filtrar_pares(numeros):
    numeros_paresA = [n for n in numeros if n % 2 == 0]
    numeros_paresB = []
    for n in numeros:
        if n % 2 == 0:
            numeros_paresB.append(n)
    return numeros_paresA, numeros_paresB


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


numeros_paresA, numeros_paresB = filtrar_pares(numeros)


print("Versión A:", numeros_paresA)
print("Versión B:", numeros_paresB)