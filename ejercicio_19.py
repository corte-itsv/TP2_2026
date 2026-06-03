def contar_palabras(texto):
    palabras = texto.lower().split()
    return len(palabras)

def palabras_unicas(texto):
    return set(texto.lower().split())

def frecuencia(texto):
    palabras = texto.lower().split()
    frec = {}

    for palabra in palabras:
        frec[palabra] = frec.get(palabra, 0) + 1

    return dict(
        sorted(frec.items(), key=lambda x: x[1], reverse=True)
    )

def palabra_mas_comun(texto):
    frec = frecuencia(texto)
    palabra = next(iter(frec))
    return palabra, frec[palabra]

def palabras_largas(texto, minimo):
    return sorted({
        palabra
        for palabra in texto.lower().split()
        if len(palabra) >= minimo
    })


# Texto de prueba
texto = """python es un lenguaje de programacion
python es facil de aprender y python es muy usado
en ciencia de datos inteligencia artificial y desarrollo web"""

# Pruebas
print("Total de palabras:", contar_palabras(texto))
print("Palabras únicas:", palabras_unicas(texto))
print("Frecuencia:", frecuencia(texto))

palabra, cantidad = palabra_mas_comun(texto)
print("Palabra más común:", palabra, "-", cantidad, "veces")

print("Palabras largas (>= 7):", palabras_largas(texto, 7))