def sin_duplicados(lista):
    resultado = []
    vistos = set()

    for elemento in lista:
        if elemento not in vistos:
            resultado.append(elemento)
            vistos.add(elemento)

    return resultado


# Pruebas
lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
nombres = ["Ana", "Luis", "Ana", "Sol", "Luis", "Marcos"]

print(sin_duplicados(lista))
print(sin_duplicados(nombres))