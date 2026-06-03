def invertir(lista):
    nueva = []
    for i in range(len(lista) - 1, -1, -1):
        nueva.append(lista[i])
    return nueva

original = [1, 2, 3, 4, 5]
letras   = ["a", "b", "c", "d"]

print(invertir(original))
print(invertir(letras))