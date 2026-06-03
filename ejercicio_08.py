def contar_frecuencia(lista_palabras):
    frecuencias = {}
    for palabra in lista_palabras:
     
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias

def palabra_mas_repetida(frecuencias):

    palabra_max = max(frecuencias, key=frecuencias.get)
    cantidad = frecuencias[palabra_max]
    return palabra_max, cantidad

palabras = ["python", "es", "genial", "python", "es", "facil", "python"]

frecuencias = contar_frecuencia(palabras)
palabra, veces = palabra_mas_repetida(frecuencias)

print(frecuencias)
print(f"La palabra más repetida es: '{palabra}' ({veces} veces)")
