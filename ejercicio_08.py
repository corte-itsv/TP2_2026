def contar_frecuencia(palabras):
    frecuencias = {}
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    return frecuencias

def palabra_mas_repetida(frecuencias):
    max_palabra = None
    max_count = 0
    for palabra, count in frecuencias.items():
        if count > max_count:
            max_count = count
            max_palabra = palabra
    return max_palabra, max_count

palabras = ["python", "es", "genial", "python", "es", "facil", "python"]

frecuencias = contar_frecuencia(palabras)
print(frecuencias)

mas_repetida, veces = palabra_mas_repetida(frecuencias)
print(f"La palabra más repetida es: '{mas_repetida}' ({veces} veces)")