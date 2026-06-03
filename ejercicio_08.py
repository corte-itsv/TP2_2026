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
    max_cantidad = -1
    for palabra, cantidad in frecuencias.items():
        if cantidad > max_cantidad:
            max_cantidad = cantidad
            max_palabra = palabra
    return max_palabra, max_cantidad

palabras = ["python", "es", "genial", "python", "es", "facil", "python"]
frecuencias_dict = contar_frecuencia(palabras)
print(frecuencias_dict)
top_palabra, top_cantidad = palabra_mas_repetida(frecuencias_dict)
print(f"La palabra más repetida es: '{top_palabra}' ({top_cantidad} veces)")
