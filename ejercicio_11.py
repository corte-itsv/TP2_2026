def sin_duplicados(lista):
    set_lista = set()
    lista_sin_repetidos = []
    for elemento in lista:
        if elemento not in set_lista:
            set_lista.add(elemento)
            lista_sin_repetidos.append(elemento)
    return lista_sin_repetidos


lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
nombres = ["Ana", "Luis", "Ana", "Sol", "Luis", "Marcos"]


print("============= LISTAS SIN DUPLICADOS ==============")


lista_sin_duplicados = sin_duplicados(lista)
print("Lista de números:", lista_sin_duplicados)
lista_sin_duplicados = sin_duplicados(nombres)
print("Lista de nombres:", lista_sin_duplicados)