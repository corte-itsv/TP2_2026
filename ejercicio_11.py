def sin_duplicados(lista):
    
    nueva_lista = []
    vistos = set()

    for elemento in lista:
            if elemento not in vistos:
                nueva_lista.append(elemento)
                vistos.add(elemento)
    return nueva_lista

lista_num = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
nombres = ["Ana", "Luis", "Ana", "Sol", "Luis", "Marcos"]

print(sin_duplicados(lista_num))
print(sin_duplicados(nombres))
        
