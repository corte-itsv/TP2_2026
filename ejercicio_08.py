persona = {
    "edad": 12,
    "nonmbre": "lucas",
    "calbicie": True,
}
#print(persona["edad"])

# print(persona["nonmbre"])
#persona["nonmbre"] = "pedro"
#print(persona["nonmbre"])
#persona["nonmbre"] = "benja"
#print(persona["nonmbre"])

def contar_frecuencia(palabras):
    diccionario = {}
    for palabra in palabras:
        if palabra not in diccionario:
            diccionario[palabra] = 1
        else:
            diccionario[palabra] = diccionario.get(palabra) + 1
    return diccionario

def palabra_mas_repetida(diccionario_de_frecuencias):
    palabra_con_mayor_frecuencia = ""
    frecuencia_de_claves = 0
    for clave, valor in diccionario_de_frecuencias.items():
        if valor > frecuencia_de_claves:
            frecuencia_de_claves = valor
            palabra_con_mayor_frecuencia = clave
    return palabra_con_mayor_frecuencia
        
def primer_elemento_suficiente(diccionario_de_frecuencias, frecuencia_minima):
    primer_clave_que_cumpla_condicion_frecuencia_minima = ""
    for clave, valor in diccionario_de_frecuencias.items():
        if valor >= frecuencia_minima:
            primer_clave_que_cumpla_condicion_frecuencia_minima = clave
            return primer_clave_que_cumpla_condicion_frecuencia_minima
            

palabras = ["python", "es", "genial", "python", "es", "facil", "python"]

diccionario_final = contar_frecuencia(palabras)
print(diccionario_final)
informacion_final = palabra_mas_repetida(diccionario_final)
print("La palabra mas repetidas es: ", informacion_final)
