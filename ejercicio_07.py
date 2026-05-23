def esta_en_lista(lista, elemento):           
    for fruta in lista: 
        if fruta == elemento:
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

