def contar_frecuencia(palabras):
    frecuencias = {}

    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1

        else:
            frecuencias[palabra] = 1

    return frecuencias

def palabra_mas_repetida(frecuencias):
    palabra_ganadora = ""
    max_frecuencia = 0

    for palabra, frecuencia in frecuencias.items():
        if frecuencia > max_frecuencia:
            max_frecuencia = frecuencia
            palabra_ganadora = palabra

    return palabra_ganadora

palabras = ["python", "es", "genial", "python", "es", "facil", "python"]

frecuencias = contar_frecuencia(palabras)
ganadora = palabra_mas_repetida(frecuencias)

print(frecuencias)
print(f"La palabra mas repetida es: '{palabra_mas_repetida(frecuencias)}' ({frecuencias[ganadora]} veces)")