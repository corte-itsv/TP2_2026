def contar_frecuencia(palabras):
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia 

def palabra_mas_repetida(frecuencias):
    max_frecuencia = 0 
    palabra_mas_comun = None
    for palabra, frecuencia in frecuencias.items():
        if frecuencia > max_frecuencia:
            max_frecuencia = frecuencia
            palabra_mas_comun = palabra
    return palabra_mas_comun, max_frecuencia 

palabras = ["python", "es", "genial", "python", "es", "facil", "python"]
frecuencias = contar_frecuencia(palabras)
palabra_comun, frecuencia_comun = palabra_mas_repetida(frecuencias)

print(f"frecuencias: {frecuencias}")
print(f"La palabra más repetida es: '{palabra_comun}' ")