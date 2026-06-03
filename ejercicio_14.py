def a_mayusculas(palabras):
    return [p.upper() for p in palabras]

def longitudes(palabras):
    return [len(p) for p in palabras]

def filtrar_largas(palabras, minimo):
    return [p for p in palabras if len(p) >= minimo]

def iniciales(palabras):
    return [p[0].upper() for p in palabras]


palabras = ["python", "programacion", "dato", "lista", "funcion", "set", "bucle"]

print(f"Mayúsculas:  {a_mayusculas(palabras)}")
print(f"Longitudes:  {longitudes(palabras)}")
print(f"Largas (>=6): {filtrar_largas(palabras, 6)}")
print(f"Iniciales:   {iniciales(palabras)}")