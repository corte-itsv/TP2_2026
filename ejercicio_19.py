texto = """python es un lenguaje de programacion
python es facil de aprender y python es muy usado
en ciencia de datos inteligencia artificial y desarrollo web"""

def contar_palabras(texto):
    lista_de_palabras_en_texto = texto.split()
    cantidad_de_palabras = 0
    for palabra in lista_de_palabras_en_texto:
        cantidad_de_palabras = cantidad_de_palabras + 1
    return cantidad_de_palabras

def listar_palabras_ordenadas_alfabeticamente(texto):
    lista_de_palabras_en_texto = texto.split()
    lista_de_palabras_en_texto_ordenadas_abc = sorted(lista_de_palabras_en_texto, key=str.lower)
    return lista_de_palabras_en_texto_ordenadas_abc

def palabras_unicas(texto):
    lista_de_palabras_en_texto = listar_palabras_ordenadas_alfabeticamente(texto)
    set_lista = set()
    cantidad_de_palabras_unicas = 0
    for palabra in lista_de_palabras_en_texto:
        if palabra not in set_lista:
            set_lista.add(palabra)
            cantidad_de_palabras_unicas = cantidad_de_palabras_unicas + 1
    return cantidad_de_palabras_unicas

def frecuencia(texto):
    frecuencias = {}
    lista_de_palabras_en_texto = listar_palabras_ordenadas_alfabeticamente(texto)
    for palabra in lista_de_palabras_en_texto:
        if palabra not in frecuencias:
            frecuencias[palabra] = 1
        else:
            frecuencias[palabra] = frecuencias[palabra] + 1
    return frecuencias

def listar_tuplas(texto):
    dict_de_frecuencias_original = frecuencia(texto)
    lista_de_tuplas = []
    for palabra, frecuencia_de_palabra in dict_de_frecuencias_original.items():
        lista_de_tuplas.append((palabra, frecuencia_de_palabra))
    lista_de_tuplas_final = sorted(lista_de_tuplas, key=lambda x: x[1], reverse=True)
    return lista_de_tuplas_final

def ordenar_diccionario_de_frecuencias(texto):
    lista_de_tuplas_final = listar_tuplas(texto)
    nuevo_dict_de_frecuencias = {}
    for (palabra, frecuencia_de_palabra) in lista_de_tuplas_final:
        nuevo_dict_de_frecuencias[palabra] = frecuencia_de_palabra
    return nuevo_dict_de_frecuencias

def imprimir_el_dict_de_frecuencias_ordenado(texto):
    nuevo_dict_de_frecuencias = ordenar_diccionario_de_frecuencias(texto)
    for palabra, frecuencia_de_palabra in nuevo_dict_de_frecuencias.items(): 
        print(f"{palabra:<15}: {frecuencia_de_palabra}")

def palabra_mas_comun(texto):
    dict_ordenado = ordenar_diccionario_de_frecuencias(texto)
    palabra_que_mas_se_repite = ""
    cantidad_de_veces_que_se_repite = 0
    for palabra, frecuencia_de_la_misma in dict_ordenado.items():
        if frecuencia_de_la_misma > cantidad_de_veces_que_se_repite:
            cantidad_de_veces_que_se_repite = frecuencia_de_la_misma
            palabra_que_mas_se_repite = palabra
    return (palabra_que_mas_se_repite, cantidad_de_veces_que_se_repite)

def palabras_largas(texto, minimo):
    lista_de_palabras_en_texto = listar_palabras_ordenadas_alfabeticamente(texto)
    lista_con_palabras_largas = []
    for palabra in lista_de_palabras_en_texto:
        if len(palabra) > minimo:
            lista_con_palabras_largas.append(palabra)
    return lista_con_palabras_largas
            

cantidad_de_palabras = contar_palabras(texto)
print("Total de palabras:", cantidad_de_palabras)

cantidad_de_palabras_unicas_en_texto = palabras_unicas(texto)
print("Palabras únicas:", cantidad_de_palabras_unicas_en_texto)

print("==== FRECUENCIAS ====")

imprimir_el_dict_de_frecuencias_ordenado(texto)

palabra_que_mas_se_repite, cantidad_de_veces_que_se_repite = palabra_mas_comun(texto)
print(f"Palabra mas común: {palabra_que_mas_se_repite} ({cantidad_de_veces_que_se_repite} veces)")
lista_con_palabras_largas = palabras_largas(texto, 7)
print(f"Palabras largas (>=7): {lista_con_palabras_largas}")