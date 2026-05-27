#i = palabra
 
palabras = ["python", "es", "genial", "python", "es", "facil", "python"]

def  contar_frecuencia(palabras):
    frecuencias = {}
    for i in palabras:
        if i not in frecuencias:
            frecuencias[i] = 1
        else:
            frecuencias[i] +=1
    return frecuencias

def palabra_mas_repetida(frecuencias):
    c_max = 0
    palabra_rep = ""
    for palabra, cantidad in frecuencias.items():
        if cantidad > c_max:
            c_max = cantidad
            palabra_rep = palabra
    return {palabra_rep: c_max}

dicc_freq = contar_frecuencia(palabras)
print(dicc_freq)

ganadora = palabra_mas_repetida(dicc_freq)

for texto_palabra, cant_veces in ganadora.items():
    print(f"La palabra más repetida es: '{texto_palabra}' ({cant_veces} veces)")