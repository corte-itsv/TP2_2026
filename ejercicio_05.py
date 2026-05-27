def filtrar_pares(numeros):
    resultado = []
    for n in numeros:
        if n % 2 == 0:
            resultado.append(n)
    return resultado

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(filtrar_pares(numeros))