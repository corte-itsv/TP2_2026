def contar_frecuencia(palabras):
    frecuencias = {}
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    return frecuencias
def palabra_mas_repetida(frecuencias):
    palabra_mayor = ""
    frecuencia_mayor = 0
    for palabra in frecuencias:
        if frecuencias[palabra] > frecuencia_mayor:
            frecuencia_mayor = frecuencias[palabra]
            palabra_mayor = palabra
    return palabra_mayor