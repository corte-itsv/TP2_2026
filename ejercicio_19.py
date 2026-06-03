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
    for palabra in palabras:
        frec[palabra] = frec.get(palabra, 0) + 1
    ordenado = dict(sorted(frec.items(), key=lambda item: (-item[1], item[0])))
    return ordenado

def palabra_mas_comun(texto):
    frec = frecuencia(texto)
    if not frec:
        return None, 0
    palabra, cantidad = next(iter(frec.items()))
    return palabra, cantidad

def palabras_largas(texto, minimo):
    palabras = texto.lower().split()
    unicas = {palabra for palabra in palabras if len(palabra) >= minimo}
    return sorted(unicas)

print(f"Total de palabras: {contar_palabras(texto)}")
print(f"Palabras únicas: {len(palabras_unicas(texto))}")
print("Frecuencias:")
for palabra, cantidad in frecuencia(texto).items():
    print(f"  {palabra:<12}: {cantidad}")

mas_comun, veces = palabra_mas_comun(texto)
print(f"Palabra más común: '{mas_comun}' ({veces} veces)")
print(f"Palabras largas (>=7): {palabras_largas(texto, 7)}")
