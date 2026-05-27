def a_mayusculas(palabras):
    return [palabra.upper() for palabra in palabras]


def longitudes(palabras):
    return [len(palabra) for palabra in palabras]


def filtrar_largas(palabras, minimo):
    return [palabra for palabra in palabras if len(palabra) >= minimo]


def iniciales(palabras):
    return [palabra[0].upper() for palabra in palabras]


palabras = ["python", "programacion", "dato", "lista", "funcion", "set", "bucle"]

print("Mayúsculas:", a_mayusculas(palabras))
print("Longitudes:", longitudes(palabras))
print("Largas (>=6):", filtrar_largas(palabras, 6))
print("Iniciales:", iniciales(palabras))