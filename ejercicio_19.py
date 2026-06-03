def contar_palabras(texto):
    return len(texto.lower().split())

def palabras_unicas(texto):
    return set(texto.lower().split())

def frecuencia(texto):
    palabras = texto.lower().split()
    frec_dict = {}
    for p in palabras:
        frec_dict[p] = frec_dict.get(p, 0) + 1

    return dict(sorted(frec_dict.items(), key=lambda x: x[1], reverse=True))

def palabra_mas_comun(texto):
    frec_dict = frecuencia(texto)

    palabra = list(frec_dict.keys())[0]
    veces = frec_dict[palabra]
    return palabra, veces

def palabras_largas(texto, minimo):
    palabras = texto.lower().split()
   
    filtradas = {p for p in palabras if len(p) >= minimo}
    return sorted(list(filtradas))


text = """python es un lenguaje de programacion
python es facil de aprender y python es muy usado
en ciencia de datos inteligencia artificial y desarrollo web"""

print(f"Total de palabras: {contar_palabras(text)}")
print(f"Palabras únicas: {len(palabras_unicas(text))}")


frecuencias_totales = frecuencia(text)
print("Frecuencias:")
for count, (p, f) in enumerate(frecuencias_totales.items()):
    if count < 4:
        print(f"  {p:<12} : {f}")
print("  ...")

comun, veces_comun = palabra_mas_comun(text)
print(f"Palabra más común: '{comun}' ({veces_comun} veces)")
print(f"Palabras largas (>=7): {palabras_largas(text, 7)}")
print()