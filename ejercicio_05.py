# Lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Version A
def filtrar_pares(numeros):
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

pares = filtrar_pares(numeros)
print(f"Version A: {pares}")

# Version B
def filtrar_paresv1(numeros):
    return [numero for numero in numeros if numero % 2 == 0]

print(f"Version B: {filtrar_paresv1(numeros)}")





