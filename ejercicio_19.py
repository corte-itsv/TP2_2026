texto = """python es un lenguaje de programacion
python es facil de aprender y python es muy usado
en ciencia de datos inteligencia artificial y desarrollo web"""


def contar_palabras(texto):
    return len(texto.lower().split())


def palabras_unicas(texto):
    return set(texto.lower().split())


def frecuencia(texto):
    palabras = texto.lower().split()

    frec = {}

    for palabra in palabras:
        frec[palabra] = frec.get(palabra, 0) + 1

    return dict(
        sorted(
            frec.items(),
            key=lambda item: item[1],
            reverse=True
        )
    )


def palabra_mas_comun(texto):
    frec = frecuencia(texto)

    palabra = next(iter(frec))
    return palabra, frec[palabra]


def palabras_largas(texto, minimo):
    return sorted(
        {
            palabra
            for palabra in texto.lower().split()
            if len(palabra) >= minimo
        }
    )


print("Total de palabras:", contar_palabras(texto))
print("Palabras únicas:", len(palabras_unicas(texto)))

print("Frecuencias:")
for palabra, cantidad in frecuencia(texto).items():
    print(f"  {palabra:<12}: {cantidad}")

palabra, veces = palabra_mas_comun(texto)

print(f"Palabra más común: '{palabra}' ({veces} veces)")
print("Palabras largas (>=7):", palabras_largas(texto, 7))