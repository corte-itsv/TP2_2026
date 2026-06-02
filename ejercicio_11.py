def sin_duplicados(lista):
    vistos = set()
    nueva = []
    for elemento in lista:
        if elemento not in vistos:
            nueva.append(elemento)
            vistos.add(elemento)
    return nueva
 
lista   = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
nombres = ["Ana", "Luis", "Ana", "Sol", "Luis", "Marcos"]
 
print("\n" + str(sin_duplicados(lista)))
print(str(sin_duplicados(nombres)))
 