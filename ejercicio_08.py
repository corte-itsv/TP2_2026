def contar_frecuencia(palabras):
    """
    Cuenta la frecuencia de aparición de palabras y retorna un diccionario.
    """
    frecuencias = {}
    for p in palabras:
        if p in frecuencias:
            frecuencias[p] += 1
        else:
            frecuencias[p] = 1
    return frecuencias

def palabra_mas_repetida(frecuencias):
    """
    Encuentra la palabra con la frecuencia más alta y la devuelve como string.
    """
    mas_repetida = None
    max_frecuencia = -1
    for palabra, freq in frecuencias.items():
        if freq > max_frecuencia:
            max_frecuencia = freq
            mas_repetida = palabra
    return mas_repetida


palabras_lista = ["python", "es", "genial", "python", "es", "facil", "python"]
dicc_frecuencias = contar_frecuencia(palabras_lista)

print(dicc_frecuencias)
palabra = palabra_mas_repetida(dicc_frecuencias)
veces = dicc_frecuencias[palabra]
print(f"La palabra más repetida es: '{palabra}' ({veces} veces)")
