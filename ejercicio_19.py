texto = """python es un lenguaje de programacion
python es facil de aprender y python es muy usado
en ciencia de datos inteligencia artificial y desarrollo web"""


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
            key=lambda item: item[1],
            reverse=True
        )
    )


def palabra_mas_comun(texto):
    frecuencias = frecuencia(texto)

    palabra = max(frecuencias, key=frecuencias.get)

    return palabra, frecuencias[palabra]


def palabras_largas(texto, minimo):
    palabras = set(texto.lower().split())

    resultado = [
        palabra
        for palabra in palabras
        if len(palabra) >= minimo
    ]

    return sorted(resultado)


print("Total de palabras:", contar_palabras(texto))

print("Palabras únicas:", len(palabras_unicas(texto)))

print("Frecuencias:")

for palabra, cantidad in frecuencia(texto).items():
    print(f"{palabra:12}: {cantidad}")

palabra, cantidad = palabra_mas_comun(texto)

print(f"\nPalabra más común: '{palabra}' ({cantidad} veces)")

print(
    "Palabras largas (>=7):",
    palabras_largas(texto, 7)
)