def contar_palabras(texto):
    palabras = texto.split()
    conteo = {}
    for palabra in palabras:
        palabra = palabra.lower().strip(".,!?;:\"()")
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo


def palabras_unicas(texto):
    palabras = texto.split()
    unicas = set()
    for palabra in palabras:
        palabra = palabra.lower().strip(".,!?;:\"()")
        unicas.add(palabra)
    return unicas


def frecuencia(texto):
    conteo = contar_palabras(texto)
    total_palabras = sum(conteo.values())
    frecuencias = {palabra: conteo[palabra] / total_palabras for palabra in conteo}
    return frecuencias


def palabra_mas_comun(texto):
    conteo = contar_palabras(texto)
    if not conteo:
        return None
    return max(conteo, key=conteo.get)


def palabras_largas(texto, minimo):
    palabras = texto.split()
    largas = set()
    for palabra in palabras:
        palabra = palabra.strip(".,!?;:\"()")
        if len(palabra) >= minimo:
            largas.add(palabra)
    return largas


texto = """python es un lenguaje de programacion
python es facil de aprender y python es muy usado
en ciencia de datos inteligencia artificial y desarrollo web"""


print("Conteo de palabras:", contar_palabras(texto))
print("Palabras únicas:", palabras_unicas(texto))
print("Frecuencia de palabras:", frecuencia(texto))
print("Palabra más común:", palabra_mas_comun(texto))
print("Palabras largas (>=6):", palabras_largas(texto, 6))      