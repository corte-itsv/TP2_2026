def invertir(lista):
    lista_invertida = []
    for i in range(len(lista) - 1, -1, -1):
        lista_invertida.append(lista[i])
    return lista_invertida

# Pruebas
original = [1, 2, 3, 4, 5]
letras   = ["a", "b", "c", "d"]

print(invertir(original))
print(invertir(letras))