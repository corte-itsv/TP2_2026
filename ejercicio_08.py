def contar_frecuencia(palabras):
    frecuencias = {}
    for i in palabras:
        if i not in frecuencias:
            frecuencias[i] = 1
        else:
            frecuencias[i] = frecuencias[i] + 1
    return frecuencias

def palabra_mas_repetida(frecuencias):
    palabra_ganadora = ""
    max_cantidad = 0  

    for palabra, cantidad in frecuencias.items():
        if cantidad > max_cantidad:
            max_cantidad = cantidad
            palabra_ganadora = palabra
            
    return palabra_ganadora


palabras = ["python", "es", "genial", "python", "es", "facil", "python"]

dicc_frecuencias = contar_frecuencia(palabras)
print(dicc_frecuencias)  

ganadora = palabra_mas_repetida(dicc_frecuencias)
veces = dicc_frecuencias[ganadora]

print(f"\nLa palabra más repetida es: '{ganadora}' ({veces} veces)")