def a_mayusculas(palabras):
    lista_en_mayusculas = []
    for palabra in palabras:
        lista_en_mayusculas.append(palabra.upper())
    return lista_en_mayusculas

def longitudes(palabras):
    lista_de_longitudes = []
    for palabra in palabras:
        longitud_de_la_palabra = len(palabra)
        lista_de_longitudes.append(longitud_de_la_palabra)
    return lista_de_longitudes

def filtrar_largas(palabras, minimo):
    palabras_con_cinco_o_mas_letras = []
    for palabra in palabras:
        if len(palabra) >= minimo:
            palabras_con_cinco_o_mas_letras.append(palabra)
    return palabras_con_cinco_o_mas_letras

def iniciales(palabras):
    iniciales_en_mayusculas = []
    palabras_en_mayusculas = a_mayusculas(palabras)
    for palabra in palabras_en_mayusculas:
        iniciales_en_mayusculas.append(palabra[0])
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