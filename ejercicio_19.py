def contar_palabras(texto):
    array_de_palabras = texto.split()
    total_de_palabras = len(array_de_palabras)
    return total_de_palabras

def palabras_unicas(texto):
    palabras_sin_repetir = set()
    lista_prolija_de_palabras_sin_repetir = []
    array_de_palabras = texto.split()
    for palabra in array_de_palabras:
        if palabra not in palabras_sin_repetir:
            palabras_sin_repetir.add(palabra)
            lista_prolija_de_palabras_sin_repetir.append(palabra)
    return lista_prolija_de_palabras_sin_repetir


def cantidad_de_palabras_unicas(lista):
    cantidad_total_de_existencias_unicas = len(lista)
    return cantidad_total_de_existencias_unicas

def existe_clave_en_diccionario(diccionario, palabra):
    for palabra_del_diccionario in diccionario:
        if palabra_del_diccionario == palabra:
            return True
    return False            

def frecuencia(texto):
    dict_frecuencia_de_palabras = {}
    array_de_palabras = texto.split()
    for palabra in array_de_palabras:
        if existe_clave_en_diccionario(dict_frecuencia_de_palabras, palabra):
            dict_frecuencia_de_palabras[palabra] = dict_frecuencia_de_palabras[palabra] +1
        else:
            dict_frecuencia_de_palabras[palabra] = 1
    dict_frecuencia_de_palabras
    lista_frecuencias = []
    for palabra, frecuencia_de_palabra in dict_frecuencia_de_palabras.items():
        if frecuencia_de_palabra not in lista_frecuencias:
            lista_frecuencias.append(frecuencia_de_palabra)
    frecuencias_orden_decreciente = sorted(lista_frecuencias, reverse=True)
    dict_frecuencias_finales_ordenadas = {}
    for frecuencia in frecuencias_orden_decreciente:
        for palabra, frecuencia_de_palabra in dict_frecuencia_de_palabras.items():
            if frecuencia_de_palabra == frecuencia:
                dict_frecuencias_finales_ordenadas[palabra] = frecuencia_de_palabra
    return dict_frecuencias_finales_ordenadas

def imprimir_diccionario_ordenado(diccionario):
    for palabra, frecuencia_de_la_misma in diccionario.items():
        print(palabra, ":", frecuencia_de_la_misma)

def palabra_mas_comun(texto):
    palabra_mas_presente = ""
    dict_palabras_y_sus_frecuencias = frecuencia(texto)
    frecuencia_ = 0
    for palabra, frecuencia_de_la_palabra in dict_palabras_y_sus_frecuencias.items():
            if frecuencia_de_la_palabra > frecuencia_:
                frecuencia_ = frecuencia_de_la_palabra
                palabra_mas_presente = palabra
    return (palabra_mas_presente, frecuencia_)

    
def palabras_largas(texto, minimo):
    lista_set = set()
    lista_final_con_siete_o_mas_letras = []
    lista_de_palabras_unicas = palabras_unicas(texto)
    for palabra in lista_de_palabras_unicas:
        if palabra not in lista_set and len(palabra) >= minimo:
            lista_set.add(palabra)
            lista_final_con_siete_o_mas_letras.append(palabra)
    lista_final_final = sorted(lista_final_con_siete_o_mas_letras)
    return lista_final_final




 
texto = """python es un lenguaje de programacion
python es facil de aprender y python es muy usado
en ciencia de datos inteligencia artificial y desarrollo web"""


cantidad_de_palabras_contadas = contar_palabras(texto)
print("Total de palabras: ", cantidad_de_palabras_contadas)

palabras_sin_repetir = palabras_unicas(texto)
cantidad_total = cantidad_de_palabras_unicas(palabras_sin_repetir)
print("Palabras únicas: ", cantidad_total)

print("Frecuencias:")
dict_ordenado_en_frecuencias_mayor_a_menor = frecuencia(texto)
imprimir_diccionario_ordenado(dict_ordenado_en_frecuencias_mayor_a_menor)

palabra_mas_repetida, frecuencia_de_la_palabra = palabra_mas_comun(texto)
print("Palabra más común: ", "'", palabra_mas_repetida, "'", "(", frecuencia_de_la_palabra, "veces )")

palabras_con_siete_o_mas_letras = palabras_largas(texto, 7)
print("Palabras largas (>=7): ", palabras_con_siete_o_mas_letras)