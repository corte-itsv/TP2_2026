def contar_palabras(texto):
    palabras = texto.lower().split()
    contador_palabras = 0
    
    for palabra in palabras:
        contador_palabras += 1

    return contador_palabras

def palabras_unicas(texto):
    palabras = texto.lower().split()
    return set(palabras)

def frecuencia(texto):
    palabras = texto.lower().split()
    frecuencias = {}

    for palabra in palabras:
        if palabra not in frecuencias:
            frecuencias[palabra] = 1
        else:
            frecuencias[palabra] += 1

    # ordenar de mayor a menor frecuencia
    frecuencias_ordenadas = dict(
        sorted(frecuencias.items(), key=lambda item: item[1], reverse=True)
    )

    return frecuencias_ordenadas

def palabra_mas_comun(texto):
    frecuencias = frecuencia(texto)

    palabra_ganadora = ""
    max_cantidad = 0

    for palabra, cantidad in frecuencias.items():
        if cantidad > max_cantidad:
            max_cantidad = cantidad
            palabra_ganadora = palabra

    return palabra_ganadora, max_cantidad

def palabras_largas(texto, minimo):
    palabras = texto.lower().split()

    lista = []

    for palabra in palabras:
        if len(palabra) >= minimo and palabra not in lista:
            lista.append(palabra)

    lista.sort()

    return lista

texto = """python es un lenguaje de programacion
python es facil de aprender y python es muy usado
en ciencia de datos inteligencia artificial y desarrollo web"""

print(f"Total de palabras: {contar_palabras(texto)}")

print(f"Palabras únicas: {len(palabras_unicas(texto))}")

print("Frecuencias:")
frecuencias = frecuencia(texto)

for palabra, cantidad in frecuencias.items():
    print(f"{palabra:15}: {cantidad}")

palabra, cantidad = palabra_mas_comun(texto)

print(f"Palabra más común: '{palabra}' ({cantidad} veces)")

print(f"Palabras largas (>=7): {palabras_largas(texto, 7)}")