def contar_palabras(texto):
    return len(texto.lower().split())

def palabras_unicas(texto):
    return set(texto.lower().split())

def frecuencia(texto):
    lista_palabras = texto.lower().split()
    dicc_frec = {}
    for p in lista_palabras:
        dicc_frec[p] = dicc_frec.get(p, 0) + 1
    return dict(sorted(dicc_frec.items(), key=lambda x: x[1], reverse=True))

def palabra_mas_comun(texto):
    dicc_frec = frecuencia(texto)
    palabra = list(dicc_frec.keys())[0]
    cantidad = list(dicc_frec.values())[0]
    return palabra, cantidad

def palabras_largas(texto, minimo):
    lista_palabras = texto.lower().split()
    largas = set()
    for p in lista_palabras:
        if len(p) >= minimo:
            largas.add(p)
    return sorted(list(largas))

texto = """python es un lenguaje de programacion
python es facil de aprender y python es muy usado
en ciencia de datos inteligencia artificial y desarrollo web"""

print(f"Total de palabras: {contar_palabras(texto)}")
print(f"Palabras únicas: {len(palabras_unicas(texto))}")
print("Frecuencias:")
frecuencias = frecuencia(texto)
for palabra, cant in list(frecuencias.items())[:5]:
    print(f"  {palabra:<13}: {cant}")
print("  ...")

comun, veces = palabra_mas_comun(texto)
print(f"Palabra más común: '{comun}' ({veces} veces)")
print(f"Palabras largas (>=7): {palabras_largas(texto, 7)}")
