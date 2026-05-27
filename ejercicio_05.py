# Versión A: usando for con append()
def filtrar_pares_a(numeros):
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

# Versión B: usando list comprehension
def filtrar_pares_b(numeros):
    return [numero for numero in numeros if numero % 2 == 0]


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print("Versión A:", filtrar_pares_a(numeros))
print("Versión B:", filtrar_pares_b(numeros))