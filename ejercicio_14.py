def a_mayusculas(palabras):
    mayusculas = []
    for palabra in palabras:
        mayusculas.append(palabra.upper())
    return mayusculas

def longitudes(palabras):
    longitudes_a = []
    for palabra in palabras:
        longitudes_a.append(len(palabra))
    return longitudes_a

def filtrar_largas(palabras, minimo):
    mas_largas = []
    for palabra in palabras:
        if len(palabra) >= minimo:
            mas_largas.append(palabra)
    return mas_largas

def iniciales(palabras):
    inicial = []
    for palabra in palabras:
        inicial.append(palabra[0].upper())
    return inicial

palabras = ["python", "programacion", "dato", "lista", "funcion", "set", "bucle"]

minimo = 6
print(f"Mayúsculas: {a_mayusculas(palabras)}")
print(f"Longitudes: {longitudes(palabras)}")
print(f"Largas (>={minimo}): {filtrar_largas(palabras, minimo)}")
print(f"Iniciales: {iniciales(palabras)}")
