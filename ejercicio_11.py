def sin_duplicados(lista):
    nueva_lista = []
    vistos = set()

    for elementos in lista:
        if elementos not in vistos:
            nueva_lista.append(elementos)
            vistos.add(elementos)
    return nueva_lista

lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
nombres = ["Ana", "Luis", "Ana", "Sol", "Luis", "Marcos"]

print(sin_duplicados(lista))
print(sin_duplicados(nombres))