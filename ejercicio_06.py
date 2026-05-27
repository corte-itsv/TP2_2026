original = [1, 2, 3, 4, 5]
letras   = ["a", "b", "c", "d"]

def invertir(lista):
    invertido = []
    for i in range(len(lista) -1, -1, -1,):
        elemento = lista[i]
        invertido.append(elemento)
    return invertido

print(invertir(original))

print(invertir(letras))
