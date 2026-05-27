def esta_en_lista(lista, elemento):

    i = 0

    largo = len(lista)
    
    while i < largo:
        if lista[i] == elemento:
              return True
        i += 1
    return False
        
def posicion_en_lista(lista, elemento):

    i = 0
    largo = len(lista)
    while i < largo:
         if lista[i] == elemento:
              return i
         i += 1
    return -1

frutas = ["manzana", "banana", "pera", "uva", "kiwi"]

print(f"¿'pera' está en la lista? {esta_en_lista(frutas, 'pera')}")
print(f"¿'mango' está en la lista? {esta_en_lista(frutas, 'mango')}")
print(f"Posición de 'uva': {posicion_en_lista(frutas, 'uva')}")
print(f"Posición de 'mango': {posicion_en_lista(frutas, 'kiwi')}")