texto = """python es un lenguaje de programacion
python es facil de aprender y python es muy usado
en ciencia de datos inteligencia artificial y desarrollo web"""


def contar_palabras(texto):
    return len(texto.lower().split())


def palabras_unicas(texto):
    return set(texto.lower().split())


def frecuencia(texto):
    palabras = texto.lower().split()
    conteo = {}
    for p in palabras:
        conteo[p] = conteo.get(p, 0) + 1
    return dict(sorted(conteo.items(), key=lambda x: x[1], reverse=True))


def palabra_mas_comun(texto):
    freq = frecuencia(texto)
    palabra = next(iter(freq))
    return palabra, freq[palabra]


def palabras_largas(texto, minimo):
    return sorted(set(p for p in texto.lower().split() if len(p) >= minimo))


# Resultados
print(f"Total de palabras: {contar_palabras(texto)}")
print(f"Palabras únicas: {len(palabras_unicas(texto))}")

print("Frecuencias:")
for palabra, cant in frecuencia(texto).items():
    print(f"  {palabra:12} : {cant}")

pal, veces = palabra_mas_comun(texto)
print(f"Palabra más común: '{pal}' ({veces} veces)")
print(f"Palabras largas (>=7): {palabras_largas(texto, 7)}")