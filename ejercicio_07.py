def esta_en_lista(lista, elemento):
    indice = 0
    while indice < len(lista):
        if lista[indice] == elemento:
            return True
        indice += 1
    return False

def posicion_en_lista(lista, elemento):
    indice = 0
    while indice < len(lista):
        if lista[indice] == elemento:
            return indice
        indice += 1
    return -1

frutas = ["manzana", "banana", "pera", "uva", "kiwi"]

print("¿Pera existe?:", esta_en_lista(frutas, "pera"))
print("¿Mango existe?:", esta_en_lista(frutas, "mango"))
print("Posicion de uva:", posicion_en_lista(frutas, "uva"))
print("Posicion de mango:", posicion_en_lista(frutas, "mango"))