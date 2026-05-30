def filtrar_pares(numeros):
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

def filtrar_pares_B(numeros):
    return [numero for numero in numeros if numero % 2 == 0]

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(f"Version A: {filtrar_pares(numeros)}")
print(f"Version B: {filtrar_pares_B(numeros)}")