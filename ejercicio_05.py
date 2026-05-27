def pares_1(numeros):
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

#version 2
def pares_2(numeros):
    return [numero for numero in numeros if numero % 2 == 0]

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print("Versión A:", pares_1(numeros))
print("Versión B:", pares_2(numeros))
