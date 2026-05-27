def contar_frecuencia(palabras):
    frecuencias = {}
    
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    
    return frecuencias


def palabra_mas_repetida(frecuencias):

    palabra_max = None
    frecuencia_max = 0
    
    for palabra, frecuencia in frecuencias.items():
        if frecuencia > frecuencia_max:
            frecuencia_max = frecuencia
            palabra_max = palabra
    
    return palabra_max, frecuencia_max



palabras = ["python", "es", "genial", "python", "es", "facil", "python"]

frecuencias = contar_frecuencia(palabras)
print(frecuencias)

palabra, veces = palabra_mas_repetida(frecuencias)
print(f"La palabra más repetida es: '{palabra}' ({veces} veces)") 

def contar_frecuencia(palabras):

    frecuencias = {}
    
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    
    return frecuencias


def palabra_mas_repetida(frecuencias):

    palabra_max = None
    frecuencia_max = 0
    
    for palabra, frecuencia in frecuencias.items():
        if frecuencia > frecuencia_max:
            frecuencia_max = frecuencia
            palabra_max = palabra
    
    return palabra_max, frecuencia_max


palabras = ["python", "es", "genial", "python", "es", "facil", "python"]

frecuencias = contar_frecuencia(palabras)
print(frecuencias)

palabra, veces = palabra_mas_repetida(frecuencias)
print(f"La palabra más repetida es: '{palabra}' ({veces} veces)")  #6767676767