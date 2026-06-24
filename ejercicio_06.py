def invertir(lista):
    elementos_invertidos = []
    for elemento in lista:
        elementos_invertidos.insert(0, elemento)
    return elementos_invertidos


original = [1, 2, 3, 4, 5]
letras   = ["a", "b", "c", "d"]
animales = ["perro", "gato", "loro"]

originales_invertidos = invertir(original)
print("Original = ", originales_invertidos)
letras_invertidas = invertir(letras)
print("Letras = ", letras_invertidas)
animales_inertidos = invertir(animales)
print("Animales = ", animales_inertidos)