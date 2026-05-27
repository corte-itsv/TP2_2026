def sin_duplicados(lista):
    vistos = set()
    nueva_lista = []

    for elemento in lista:
        if elemento not in vistos:
            vistos.add(elemento)
            nueva_lista.append(elemento)

    return nueva_lista


lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
nombres = ["Ana", "Luis", "Ana", "Sol", "Luis", "Marcos"]

print(sin_duplicados(lista))
print(sin_duplicados(nombres))