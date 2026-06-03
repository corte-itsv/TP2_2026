def contar_frecuencia(palabras):
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias

def palabra_mas_repetida(frecuencias):
    max_palabra = None
    max_votos = -1
    for palabra, cant in frecuencias.items():
        if cant > max_votos:
            max_votos = cant
            max_palabra = palabra
    return max_palabra

# Pruebas
palabras = ["python", "es", "genial", "python", "es", "facil", "python"]
frec = contar_frecuencia(palabras)
print(frec)

top_palabra = palabra_mas_repetida(frec)
print(f"La palabra más repetida es: '{top_palabra}' ({frec[top_palabra]} veces)")