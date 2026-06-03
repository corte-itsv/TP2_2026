def contar_palabras(texto):
    return len(texto.lower().split())

def palabras_unicas(texto):
    return set(texto.lower().split())

def frecuencia(texto):
    palabras = texto.lower().split()
    frec = {}
    for p in palabras:
        frec[p] = frec.get(p, 0) + 1
    return dict(sorted(frec.items(), key=lambda x: x[1], reverse=True))

def palabra_mas_comun(texto):
    frec_dict = frecuencia(texto)
    top_palabra = list(frec_dict.keys())[0]
    return top_palabra, frec_dict[top_palabra]

def palabras_largas(texto, minimo):
    filtradas = {p for p in texto.lower().split() if len(p) >= minimo}
    return sorted(list(filtradas))

# Pruebas
texto = """python es un lenguaje de programacion
python es facil de aprender y python es muy usado
en ciencia de datos inteligencia artificial y desarrollo web"""

print(f"Total de palabras: {contar_palabras(texto)}")
print(f"Palabras únicas: {len(palabras_unicas(texto))}")
print("Frecuencias:")
frecuencias_todas = frecuencia(texto)
for pal, cant in list(frecuencias_todas.items())[:4]:
    print(f"  {pal:<13}: {cant}")
print("  ...")

p_comun, c_comun = palabra_mas_comun(texto)
print(f"Palabra más común: '{p_comun}' ({c_comun} veces)")
print(f"Palabras largas (>=7): {palabras_largas(texto, 7)}")