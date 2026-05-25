def contar_palabras(texto):
    contador_palabras=0
    for palabra in texto:
        contador_palabras+=1
    return contar_palabras

def palabras_unicas(texto):
    lista_palabras_con_repeticion=[]
    for palabra in texto:
        lista_palabras_con_repeticion.append(palabra)
    return lista_palabras_con_repeticion
    sin_rep=set(lista_palabras_con_repeticion)
    contador_palabras_sin_rep=0
    for palabra in sin_rep:
        contador_palabras_sin_rep+=1
    return condor_palabras_sin_rep



def frecuencia(texto):
    frecuencias = {}
    for palabra in texto:
        if palabra not in frecuencias:
            frecuencias[palabra] = 1
        else:
            frecuencias[palabra] = frecuencias[palabra] + 1
    return frecuencias

def palabra_mas_comun(texto):
    palabra_ganadora = ""
    max_cantidad = 0  
    for palabra, cantidad in frecuencias.items():
        if cantidad > max_cantidad:
            max_cantidad = cantidad
            palabra_ganadora = palabra
    return palabra_ganadora

def palabras_largas(texto, minimo):
    for palabra in texto:
        if len(palabra)>minimo:
            texto.lower().split()

texto = """python es un lenguaje de programacion
python es facil de aprender y python es muy usado
en ciencia de datos inteligencia artificial y desarrollo web"""
print(f"Total de palabras: {contar_palabras(texto)} ")
print(f"Palabras unicas: {palabras_unicas(texto)} ")
for palabra, frecuencia in frecuencias:
    print(palabra, frecuencia)
print(f"Palabras mas largas: {palabras_largas(texto, minimo)}")