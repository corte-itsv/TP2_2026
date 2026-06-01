def invertir(lista):
    invertida = []

    for i in range(len(lista) - 1, -1, -1):
        invertida.append(lista[i])

    return invertida

numeros = [1, 2, 3, 4, 5]

resultado = invertir(numeros)

print(resultado)