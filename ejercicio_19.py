texto = """python es un lenguaje de programacion
python es facil de aprender y python es muy usado
en ciencia de datos inteligencia artificial y desarrollo web"""

def contar_palabras(texto):
    palabras = texto.lower().split()
    return len(palabras)


def palabras_unicas(texto):
    palabras = texto.lower().split()
    return set(palabras)


def frecuencia(texto):
    palabras = texto.lower().split()
    frec = {}
    for p in palabras:
        frec[p] = frec.get(p, 0) + 1
    return dict(sorted(frec.items(), key=lambda x: x[1], reverse=True))

def palabra_mas_comun(texto):
    frec = frecuencia(texto)
    palabra = max(frec, key=frec.get)
    return palabra, frec[palabra]


def palabras_largas(texto, minimo):
    palabras = texto.lower().split()
    largas = {p for p in palabras if len(p) >= minimo}
    return sorted(largas)



print("Total de palabras:", contar_palabras(texto))
print("Palabras únicas:", len(palabras_unicas(texto)))

print("Frecuencias:")
for palabra, cant in frecuencia(texto).items():
    print(f"  {palabra:<12}: {cant}")

comun, veces = palabra_mas_comun(texto)
print(f"Palabra más común: '{comun}' ({veces} veces)")

print("Palabras largas (>=7):", palabras_largas(texto, 7))