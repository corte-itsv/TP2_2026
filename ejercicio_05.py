def filtrar_pares_a(numeros):
    pares = []
    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
    return pares


def filtrar_pares_b(numeros):
    return [n for n in numeros if n % 2 == 0]


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(f"Versión A: {filtrar_pares_a(numeros)}")
print(f"Versión B: {filtrar_pares_b(numeros)}")