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

    for palabra in frecuencias:
        if frecuencias[palabra] > mayor_cantidad:
            mayor_cantidad = frecuencias[palabra]
            mayor_palabra = palabra

    return mayor_palabra


# Lista de prueba
palabras = ["python", "es", "genial", "python", "es", "facil", "python"]

# Contar frecuencias
frecuencias = contar_frecuencia(palabras)

# Mostrar resultados
print("Frecuencias:", frecuencias)
print("Palabra más repetida:", palabra_mas_repetida(frecuencias))