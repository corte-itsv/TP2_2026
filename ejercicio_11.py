def sin_duplicados(lista):
    resultado = []
    vistos = set()

    for numero in lista:
        if numero not in vistos:
            resultado.append(numero)
            vistos.add(numero)

    return resultado

lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
nombres = ["Ana", "Luis", "Ana", "Sol", "Luis", "Marcos"]

print(sin_duplicados(lista))
print(sin_duplicados(nombres))

