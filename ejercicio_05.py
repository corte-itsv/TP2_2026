def filtrar_pares_version_a(numeros):
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares


def filtrar_pares_version_b(numeros):
    return [numero for numero in numeros if numero % 2 == 0]


if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    resultado_a = filtrar_pares_version_a(numeros)
    resultado_b = filtrar_pares_version_b(numeros)

    print(f"Versión A: {resultado_a}")
    print(f"Versión B: {resultado_b}")
