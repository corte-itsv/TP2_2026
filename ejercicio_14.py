def a_mayusculas(palabras):
    lista_en_mayusculas = [palabra.upper() for palabra in palabras]
    return lista_en_mayusculas

def longitudes(palabras):
    lista_de_longitudes = [len(palabra) for palabra in palabras]
    return lista_de_longitudes

    
def filtrar_largas(palabras, minimo):
    palabras_con_cinco_o_mas_letras =  [palabra for palabra in palabras if len(palabra) >= minimo]
    return palabras_con_cinco_o_mas_letras

def iniciales(palabras):
    palabras_en_mayusculas = a_mayusculas(palabras)
    iniciales_en_mayusculas = [palabra[0] for palabra in palabras_en_mayusculas]
    return iniciales_en_mayusculas


palabras = ["python", "programacion", "dato", "lista", "funcion", "set", "bucle"]

lista_de_palabras_en_mayusculas = a_mayusculas(palabras)
print("Mayúsculas:", lista_de_palabras_en_mayusculas)

lista_de_longitudes = longitudes(palabras)
print("Longitudes:", lista_de_longitudes)

palabras_filtradas = filtrar_largas(palabras, 6)
print("Largas (>= 6):", palabras_filtradas)

iniciales_en_mayusculas = iniciales(palabras)
print("Iniciales:", iniciales_en_mayusculas)