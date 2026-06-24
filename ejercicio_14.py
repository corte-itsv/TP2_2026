def a_mayusculas(palabras):
    lista_con_palabras_en_mayusculas = [palabra.upper() for palabra in palabras]
    return lista_con_palabras_en_mayusculas

def lista_de_longitudes(palabras):
    lista_de_longitudes = [len(palabra) for palabra in palabras]
    return lista_de_longitudes

def filtrar_largas(palabras, minimo):
    palabras_largas = [palabra for palabra in palabras if len(palabra) >= minimo]
    return palabras_largas

# devuelve la primer letra en mayuscula de cada palabra en palabras
def iniciales(palabras):
    primer_letra_en_may_de_cada_palabra = [palabra[0].upper() for palabra in palabras]
    return primer_letra_en_may_de_cada_palabra

palabras = ["python", "programacion", "dato", "lista", "funcion", "set", "bucle"]


palabras_en_mayusculas = a_mayusculas(palabras)
print("Mayúsculas: ", palabras_en_mayusculas)

longitudes_listadas = lista_de_longitudes(palabras)
print("Longitudes: ", longitudes_listadas)

palabras_filtradas_segun_largo = filtrar_largas(palabras, 6)
print("Largas (>=6): ", palabras_filtradas_segun_largo)

primer_letra_de_cada_palabra = iniciales(palabras)
print("Iniciales: ", primer_letra_de_cada_palabra)