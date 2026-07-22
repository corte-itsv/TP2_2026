def contar_frecuencia(lista):
    frecuencias = {}
    for palabra in lista:
        if palabra not in frecuencias:
            frecuencias[palabra] = 1
        else:
            frecuencias[palabra] = frecuencias[palabra] + 1
    return frecuencias

def palabra_mas_repetida(frecuencias):
    la_mas_repetida = ""
    hipotesis_de_frecuencia = 0
    for palabra, frecuencia in frecuencias.items():
        if frecuencia > hipotesis_de_frecuencia:
            hipotesis_de_frecuencia = frecuencia
            la_mas_repetida = palabra
    return (la_mas_repetida, hipotesis_de_frecuencia)


palabras = ["python", "es", "genial", "python", "es", "facil", "python"]


print("========== DICCIONARIO DE FRECUENCIAS ==========")

frecuencias = contar_frecuencia(palabras)
print(frecuencias)


print("============ PALABRA MÁS FRECUENTE =============")

la_mas_repetida, su_frecuencia = palabra_mas_repetida(frecuencias)
print("La palabra mas repetida es:", la_mas_repetida, "(", su_frecuencia, "veces)")