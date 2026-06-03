def contar_frecuencia(palabras):
    frec = {}
    for p in palabras:
        if p in frec:
            frec[p] += 1
        else:
            frec[p] = 1
    return frec


def palabra_mas_repetida(frecuencias):
    mayor = 0
    palabra = ""
    for p in frecuencias:
        if frecuencias[p] > mayor:
            mayor = frecuencias[p]
            palabra = p
    return palabra, mayor

palabras = ["python", "es", "genial", "python", "es", "facil", "python"]
f = contar_frecuencia(palabras)
print(f)
p, c = palabra_mas_repetida(f)

print("La palabra más repetida es:", "'" + p + "'", "(", c, "veces )")