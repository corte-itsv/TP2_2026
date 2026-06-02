def contar_palabras(texto):
    return len(texto.lower().split())

def palabras_unicas(texto):
    return set(texto.lower().split())

def frecuencia(texto):
    palabras = texto.lower().split()

    frecuencias = {}

    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

    return dict(
        sorted(
            frecuencias.items(),
            key=lambda x: x[1],
            reverse=True
        )
    )

def palabra_mas_comun(texto):
    frec = frecuencia(texto)
    return max(frec.items(), key=lambda x: x[1])

def palabras_largas(texto, minimo):
    return sorted(
        {
            palabra
            for palabra in texto.lower().split()
            if len(palabra) >= minimo
        }
    )


texto = """python es un lenguaje de programacion
python es facil de aprender y python es muy usado
en ciencia de datos inteligencia artificial y desarrollo web"""

print("Total de palabras:", contar_palabras(texto))
print("Palabras únicas:", len(palabras_unicas(texto)))

frec = frecuencia(texto)

print("Frecuencias:")
for palabra, cantidad in frec.items():
    print(f"{palabra:12}: {cantidad}")

palabra, veces = palabra_mas_comun(texto)

print(f"\nPalabra más común: '{palabra}' ({veces} veces)")
print(
    "Palabras largas (>=7):",
    palabras_largas(texto, 7)
)