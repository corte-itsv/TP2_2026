def invertir(lista):
    invertida = []
    for i in range(len(lista)-1, -1, -1):
        invertida.append(lista[i])
    return invertida
original = [1, 2, 3, 4, 5]
letras   = ["a", "b", "c", "d"]
print("Invertida:", invertir(original))
print("Invertida:", invertir(letras))
