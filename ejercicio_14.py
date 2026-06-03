def a_mayusculas(palabras):
    return [p.upper() for p in palabras]

def longitudes(palabras):
    return [len(p) for p in palabras]

def filtrar_largas(palabras, minimo):
    return [p for p in palabras if len(p) >= minimo]

def iniciales(palabras):
    return [p[0].upper() for p in palabras]

palabras = ["python", "programacion", "dato", "lista", "funcion", "set", "bucle"]

print("Mayúsculas:", a_mayusculas(palabras))
print("Longitudes:", longitudes(palabras))
print("Largas (>=6):", filtrar_largas(palabras, 6))
print("Iniciales:", iniciales(palabras))
