def esta_en_lista(lista, elemento):
    for x in lista:
        if x == elemento:
            return True    
    return False
    
def posicion_en_lista(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:  
            return i            
    return -1

frutas = ["manzana", "banana", "pera", "uva", "kiwi"]


print(f"¿'pera' está en la lista? {esta_en_lista(frutas, 'pera')}")
print(f"¿'mango' está en la lista? {esta_en_lista(frutas, 'mango')}")
print(f"Posición de 'uva': {posicion_en_lista(frutas, 'uva')}")
print(f"Posición de 'mango': {posicion_en_lista(frutas, 'mango')}")
def a_mayusculas(palabras):
    return [palabra.upper() for palabra in palabras]  #

def longitudes(palabras):
    return [len(palabra) for palabra in palabras]

def filtrar_largas(palabras, minimo):
    return [palabra for palabra in palabras if len(palabra) >= minimo]

def iniciales(palabras): 
    return [palabra[0].upper() for palabra in palabras]  


palabras = ["python", "programacion", "dato", "lista", "funcion", "set", "bucle"]
minimo = 6

print(f"Mayusculas: {a_mayusculas(palabras)}")
print(f"Longitudes: {longitudes(palabras)}")
print(f"Minimo (>={minimo}): {filtrar_largas(palabras, minimo)}")
print(f"Iniciales: {iniciales(palabras)}") 