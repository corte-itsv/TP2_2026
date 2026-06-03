def invertir(lista):
    nueva_lista= []
    for elemento in lista:
        nueva_lista.insert(0, elemento)
    return nueva_lista

original = [1, 2, 3, 4, 5]
letras = ["a", "b", "c", "d"]

invertida_numeros = invertir(original)
invertida_letras = invertir(letras)

print(invertida_numeros)
print(invertida_letras)