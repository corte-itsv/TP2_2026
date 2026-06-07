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
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return dict(sorted(conteo.items(), key=lambda x: x[1], reverse=True))

def palabra_mas_comun(texto):
    freq = frecuencia(texto)
    palabra = max(freq, key=freq.get)
    return palabra, freq[palabra]

def palabras_largas(texto, minimo):
    return sorted(set(p for p in texto.lower().split() if len(p) >= minimo))

# Salida
print(f"Total de palabras: {contar_palabras(texto)}")
print(f"Palabras únicas: {len(palabras_unicas(texto))}")

print("Frecuencias:")
freq = frecuencia(texto)
for palabra, cantidad in freq.items():
    print(f"  {palabra:<12}: {cantidad}")

mas_comun, veces = palabra_mas_comun(texto)
print(f"\nPalabra más común: '{mas_comun}' ({veces} veces)")
print(f"Palabras largas (>=7): {palabras_largas(texto, 7)}")