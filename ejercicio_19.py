texto = """python es un lenguaje de programacion
python es facil de aprender y python es muy usado
en ciencia de datos inteligencia artificial y desarrollo web"""
 
def contar_palabras(texto):
    palabras = texto.lower().split()
    return len(palabras)
 
def palabras_unicas(texto):
    return set(texto.lower().split())
 
def frecuencia(texto):
    palabras = texto.lower().split()
    freq = {}
    for p in palabras:
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    freq_ordenado = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
    return freq_ordenado
 
def palabra_mas_comun(texto):
    freq = frecuencia(texto)
    palabra = ""
    maximo = 0
    for p in freq:
        if freq[p] > maximo:
            maximo = freq[p]
            palabra = p
    return palabra, maximo
 
def palabras_largas(texto, minimo):
    palabras = texto.lower().split()
    largas = []
    for p in palabras:
        if len(p) >= minimo and p not in largas:
            largas.append(p)
    return sorted(largas)
 
print("\nTotal de palabras: " + str(contar_palabras(texto)))
print("Palabras únicas: " + str(len(palabras_unicas(texto))))
print("Frecuencias:")
for palabra, cant in frecuencia(texto).items():
    print("  " + palabra.ljust(14) + ": " + str(cant))
p, v = palabra_mas_comun(texto)
print("Palabra más común: '" + p + "' (" + str(v) + " veces)")
print("Palabras largas (>=7): " + str(palabras_largas(texto, 7)))