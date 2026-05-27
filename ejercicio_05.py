def filtrar_pares_for(numeros):
    pares = []

    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)

    return pares


def filtrar_pares_comprehension(numeros):
    return [numero for numero in numeros if numero % 2 == 0]


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

version_a = filtrar_pares_for(numeros)
version_b = filtrar_pares_comprehension(numeros)

print("Versión A:", version_a)
print("Versión B:", version_b)