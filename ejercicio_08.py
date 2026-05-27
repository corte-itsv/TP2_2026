def contar_frecuencia(palabras):
    frecuencias = {}
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    return frecuencias

def palabra_mas_repetida(frecuencias):
    if not frecuencias:
        return (None,0)
    
    palabra_max = None
    max_cantidad = -1

    for palabra, cantidad in frecuencias.items():
        if cantidad > max_cantidad:
            max_cantidad = cantidad
            palabra_max = palabra
    return (palabra_max, max_cantidad)

palabras = ["python", "es", "genial", "python", "es", "facil", "python"]

dicc_frecuencias = contar_frecuencia(palabras)
print(dicc_frecuencias)

palabra, conteo = palabra_mas_repetida(dicc_frecuencias)
print(f"La palabra más repetida es: '{palabra}' ({conteo} veces)")