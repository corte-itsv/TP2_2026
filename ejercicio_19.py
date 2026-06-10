def contar_palabras(texto):
    palabras = texto.split()
    conteo = {}
    for palabra in palabras:
        palabra = palabra.lower().strip(".,!?;:\"()")
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return len(conteo) 


def frecuencia(texto):
    palabras = texto.split()
    conteo = {}
    for palabra in palabras:
        palabra = palabra.lower().strip(".,!?;:\"()")
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return dict(sorted(conteo.items(), key=lambda x: x[1], reverse=True))


def palabra_mas_comun(texto):
    conteo = frecuencia(texto)  
    if not conteo:
        return None
    palabra = max(conteo, key=conteo.get)
    return (palabra, conteo[palabra])


def palabras_largas(texto, minimo):
    palabras = texto.split()
    largas = []
    for palabra in palabras:
        palabra = palabra.lower().strip(".,!?;:\"()")
        if len(palabra) >= minimo and palabra not in largas:
            largas.append(palabra)
    return sorted(largas)  


texto = """python es un lenguaje de programacion
python es facil de aprender y python es muy usado
en ciencia de datos inteligencia artificial y desarrollo web"""


print("Conteo de palabras:", contar_palabras(texto))
print("Frecuencia de palabras:", frecuencia(texto))
print("Palabra más común:", palabra_mas_comun(texto))
print("Palabras largas (>=6):", palabras_largas(texto, 6))      