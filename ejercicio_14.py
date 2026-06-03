def a_mayusculas(palabras):
    return [palabra.upper() for palabra in palabras]  #

def longitudes(palabras):
    return [len(palabra) for palabra in palabras]

def filtrar_largas(palabras, minimo):
    return [palabra for palabra in palabras if len(palabra) >= minimo]

def iniciales(palabras): 
    return [palabra[0].upper() for palabra in palabras]  


palabras = ["python", "programacion", "dato", "lista", "funcion", "set", "bucle"]
minimo = 6

print(f"Mayusculas: {a_mayusculas(palabras)}")
print(f"Longitudes: {longitudes(palabras)}")
print(f"Minimo (>={minimo}): {filtrar_largas(palabras, minimo)}")
print(f"Iniciales: {iniciales(palabras)}") 