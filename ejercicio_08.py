palabras = ["python", "es", "genial", "python", "es", "facil", "python"]

def contar_frecuencia(palabras):
    frecuencias = dict()
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    return frecuencias

def palabra_mas_repetida(frecuencias):
    palabra_max = None
    max_count = 0
    for palabra, count in frecuencias.items():
        if count > max_count:
            max_count = count
            palabra_max = palabra
    return palabra_max          # <-- solo la palabra, sin el número

frecuencias = contar_frecuencia(palabras)
print(frecuencias)

palabra = palabra_mas_repetida(frecuencias)
print(f"La palabra más repetida es: '{palabra}' ({frecuencias[palabra]} veces)")