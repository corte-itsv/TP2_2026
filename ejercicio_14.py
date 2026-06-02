def a_mayusculas(palabras):
    return [p.upper() for p in palabras]
 
def longitudes(palabras):
    return [len(p) for p in palabras]
 
def filtrar_largas(palabras, minimo):
    return [p for p in palabras if len(p) >= minimo]
 
def iniciales(palabras):
    return [p[0].upper() for p in palabras]
 
palabras = ["python", "programacion", "dato", "lista", "funcion", "set", "bucle"]
 
print("\nMayúsculas: " + str(a_mayusculas(palabras)))
print("Longitudes: " + str(longitudes(palabras)))
print("Largas (>=6): " + str(filtrar_largas(palabras, 6)))
print("Iniciales: " + str(iniciales(palabras)))

#Este es el verdadero ejercicio 14, en el commit del ej 13 puse que era el 14, pero este es el 14.