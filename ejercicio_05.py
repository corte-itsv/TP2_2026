def filtrar_pares(numeros):
    pares = []

    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)

    return pares


# Versión B: usando list comprehension
def filtrar_pares_comprehension(numeros):
    return [numero for numero in numeros if numero % 2 == 0]


# Lista de prueba
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Probar ambas funciones
print("Versión A:", filtrar_pares(numeros))
print("Versión B:", filtrar_pares_comprehension(numeros))