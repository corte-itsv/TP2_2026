def a_mayusculas(palabras):
    return [p.upper() for p in palabras]

def longitudes(palabras):
    return [len(p) for p in palabras]

def filtrar_largas(palabras, minimo):
    return [p for p in palabras if len(p) >= minimo]

def iniciales(palabras):
    return [p[0].upper() for p in palabras]


palabras_ej14 = ["python", "programacion", "dato", "lista", "funcion", "set", "bucle"]

print(f"Mayúsculas: {a_mayusculas(palabras_ej14)}")
print(f"Longitudes: {longitudes(palabras_ej14)}")
print(f"Largas (>=6): {filtrar_largas(palabras_ej14, 6)}")
print(f"Iniciales: {iniciales(palabras_ej14)}")
