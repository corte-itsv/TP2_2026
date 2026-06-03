
def sin_duplicados(lista):

    vistos = set()
    resultado = []
    for item in lista:
        if item not in vistos:
            vistos.add(item)
            resultado.append(item)
    return resultado


lista_nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
lista_nomb = ["Ana", "Luis", "Ana", "Sol", "Luis", "Marcos"]

print(sin_duplicados(lista_nums))
print(sin_duplicados(lista_nomb))