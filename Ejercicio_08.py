def contar_frecuencia(palabras):
    frecuencias = {}
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    return frecuencias

def palabra_mas_repetida(frecuencias):
    mas_repetida = None
    for palabra in frecuencias:
        if mas_repetida is None or frecuencias[palabra] > frecuencias[mas_repetida]:
            mas_repetida = palabra
    return mas_repetida

palabras = ["python", "es", "genial", "python", "es", "facil", "python"]

frecuencias = contar_frecuencia(palabras)
print(frecuencias)

mas_repetida = palabra_mas_repetida(frecuencias)
print(f"La palabra más repetida es: '{mas_repetida}' ({frecuencias[mas_repetida]} veces)")