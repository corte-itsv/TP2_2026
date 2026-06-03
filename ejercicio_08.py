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
    mayor = 0
    for palabra, cantidad in frecuencias.items():
        if cantidad > mayor:
            mayor = cantidad
            mas_repetida = palabra
    return mas_repetida


palabras = ["python", "es", "genial", "python", "es", "facil", "python"]

frecuencias = contar_frecuencia(palabras)
print(frecuencias)

palabra = palabra_mas_repetida(frecuencias)
print(f"La palabra más repetida es: '{palabra}' ({frecuencias[palabra]} veces)")