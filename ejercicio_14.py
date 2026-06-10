def a_mayusculas(palabras):
    return [palabra.upper() for palabra in palabras]


def longitudes(palabras):
    return [len(palabra) for palabra in palabras]


def filtrar_largas(palabras, minimo):
    return [palabra for palabra in palabras if len(palabra) >= minimo]


def iniciales(palabras):
    return [palabra[0] for palabra in palabras if palabra]


palabras = ["python", "programacion", "dato", "lista", "funcion", "set", "bucle"]

 
print(f"Mayúsculas: {a_mayusculas(palabras)}")
print(f"longitudes: {longitudes(palabras)}")
print(f"Largas (>=6): {filtrar_largas(palabras, 6)}")
print(f"Iniciales: {iniciales(palabras)}")

