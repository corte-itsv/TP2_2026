def sin_duplicados(lista):
    lista_nueva = []
    vistos = set()
    for i in lista:
        if i not in vistos:
            lista_nueva.append(i)
            vistos.add(i)
        else:
            del i
    return lista_nueva
    
lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
nombres = ["Ana", "Luis", "Ana", "Sol", "Luis", "Marcos"]

print(sin_duplicados(lista))
print(sin_duplicados(nombres))
