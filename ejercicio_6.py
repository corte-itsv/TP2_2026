def invertir(lista):
    invertida = []

    for i in range(len(lista) - 1, -1, -1):
        invertida.append(lista[i])

    return invertida


# Listas de prueba
original = [1, 2, 3, 4, 5]
letras = ["a", "b", "c", "d"]

# Pruebas
print("Lista original invertida:", invertir(original))
print("Lista de letras invertida:", invertir(letras))