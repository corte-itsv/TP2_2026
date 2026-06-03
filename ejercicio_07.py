def esta_en_lista(lista, elemento):
    for item in lista:
      if item == elemento: 
       return True
    return False


def posicion_en_lista(lista, elemento):
      for Ñ in range (len(lista)):
        if lista[Ñ] == elemento:
            return Ñ
      return -1
      

frutas = ["manzana", "banana", "pera", "uva", "kiwi"]


print("¿'pera' esta en la lista?", esta_en_lista(frutas, "pera"))
print("¿'mango' está en la lista?", esta_en_lista(frutas, "mango"))
print("Posición de 'uva':", posicion_en_lista(frutas, "uva"))
print("Posición de 'mango':", posicion_en_lista(frutas, "mango"))

