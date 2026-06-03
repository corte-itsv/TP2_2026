def contar_palabras(texto):
    return len(texto.lower().split())


def palabras_unicas(texto):
    return set(texto.lower().split())


def frecuencia(texto):
    palabras = texto.lower().split()
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return dict(sorted(frecuencias.items(), key=lambda x: x[1], reverse=True))


def palabra_mas_comun(texto):
    frecuencias = frecuencia(texto)
    palabra = max(frecuencias, key=frecuencias.get)
    return palabra, frecuencias[palabra]


def palabras_largas(texto, minimo):
    palabras = texto.lower().split()
    filtradas = {palabra for palabra in palabras if len(palabra) >= minimo}
    return sorted(list(filtradas))


texto = """python es un lenguaje de programacion
python es facil de aprender y python es muy usado
en ciencia de datos inteligencia artificial y desarrollo web"""

print(f"Total de palabras: {contar_palabras(texto)}")
print(f"Palabras únicas: {len(palabras_unicas(texto))}")

print("Frecuencias:")
frecuencias = frecuencia(texto)
for palabra, cant in frecuencias.items():
    print(f"  {palabra:<13}: {cant}")

mas_comun, cant_mas_comun = palabra_mas_comun(texto)
print(f"Palabra más común: '{mas_comun}' ({cant_mas_comun} veces)")

largas = palabras_largas(texto, 7)
print(f"Palabras largas (>=7): {largas}")