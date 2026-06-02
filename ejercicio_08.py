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
    max_cantidad = 0

    for palabra, cantidad in frecuencias.items():
        if cantidad > max_cantidad:
            max_palabra = palabra
            max_cantidad = cantidad

    return max_palabra