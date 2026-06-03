def contar_frecuencia(palabras):
    frecuencias = {}

    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1

    return frecuencias


def palabra_mas_repetida(frecuencias):
    mayor_palabra = ""
    mayor_cantidad = 0

    for palabra, cantidad in frecuencias.items():
        if cantidad > mayor_cantidad:
            mayor_palabra = palabra
            mayor_cantidad = cantidad

    return mayor_palabra, mayor_cantidad


palabras = ["python", "es", "genial", "python", "es", "facil", "python"]

frecuencias = contar_frecuencia(palabras)

print(frecuencias)

palabra, cantidad = palabra_mas_repetida(frecuencias)

print(f"La palabra más repetida es: '{palabra}' ({cantidad} veces)")