def contar_palabras(texto):
    return len(texto.lower().split())


def palabras_unicas(texto):
    return set(texto.lower().split())


def frecuencia(texto):
    palabras = texto.lower().split()
    freq = {}
    for palabra in palabras:
        freq[palabra] = freq.get(palabra, 0) + 1
    return dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))


def palabra_mas_comun(texto):
    freq = frecuencia(texto)
    palabra = next(iter(freq))
    return palabra, freq[palabra]


def palabras_largas(texto, minimo):
    return sorted(set(p for p in texto.lower().split() if len(p) >= minimo))


texto = """python es un lenguaje de programacion
python es facil de aprender y python es muy usado
en ciencia de datos inteligencia artificial y desarrollo web"""

print(f"Total de palabras: {contar_palabras(texto)}")
print(f"Palabras únicas: {len(palabras_unicas(texto))}")
print("Frecuencias:")
for palabra, cantidad in frecuencia(texto).items():
    print(f"  {palabra:<13}: {cantidad}")
palabra, cantidad = palabra_mas_comun(texto)
print(f"Palabra más común: '{palabra}' ({cantidad} veces)")
print(f"Palabras largas (>=7): {palabras_largas(texto, 7)}")