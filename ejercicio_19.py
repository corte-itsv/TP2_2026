def contar_palabras(texto):
    palabras = texto.lower().split()
    return len(palabras)


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
            
    frecuencias_ordenadas = dict(sorted(frecuencias.items(), key=lambda item: item[1], reverse=True))
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
    largas = set()
    
    for palabra in palabras:
        if len(palabra) >= minimo:
            largas.add(palabra)
            
    return sorted(list(largas))


texto = """python es un lenguaje de programacion
python es facil de aprender y python es muy usado
en ciencia de datos inteligencia artificial y desarrollo web"""

minimo = 7

print(f"Total de palabras: {contar_palabras(texto)}")
print(f"Palabras únicas: {len(palabras_unicas(texto))}")

print("Frecuencias:")
dicc_frecuencias = frecuencia(texto)
for palabra, cant in dicc_frecuencias.items():
    print(f"  {palabra:<14} : {cant}")

mas_comun, repeticiones = palabra_mas_comun(texto)
print(f"Palabra más común: '{mas_comun}' ({repeticiones} veces)")

print(f"Palabras largas (>={minimo}): {palabras_largas(texto, minimo)}")