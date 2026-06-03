def invertir(lista):
    nueva_lista = []

    for i in range(len(lista) - 1, -1, -1):
        nueva_lista.append(lista[i])

    return nueva_lista

original = [1, 2, 3, 4, 5]
letras   = ["a", "b", "c", "d"]

print(invertir(original))
print(invertir(letras))