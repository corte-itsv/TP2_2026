def esta_en_lista(lista, elemento_a_encontrar):
    respuesta = False
    for elemento in lista:
        if elemento == elemento_a_encontrar:
            respuesta = True
    return respuesta 

def posicion_en_lista_1(lista, elemento_a_encontrar):
    posicion = -1
    contador_de_vueltas = 0
    for elemento in lista:
        if elemento == elemento_a_encontrar:
            return contador_de_vueltas 
        else:
            contador_de_vueltas = contador_de_vueltas + 1
    return posicion

def posicion_en_lista(lista, elemento_a_encontrar):
    posicion = -1 # hip
    contador_de_vueltas = 0
    for elemento in lista:
        if elemento == elemento_a_encontrar:
            posicion = contador_de_vueltas
            break 
        else:
            contador_de_vueltas = contador_de_vueltas + 1
    return posicion


frutas = ["manzana", "banana", "pera", "uva", "kiwi"]


respuesta_final = esta_en_lista(frutas, "pera")
print("¿'pera' está en la lista frutas? ", respuesta_final)
respuesta_final = esta_en_lista(frutas, "mango")
print("¿'mango' está en la lista frutas? ", respuesta_final)
posicion_final_del_elemento = posicion_en_lista(frutas, "pera")
print("Posición de uva = ", posicion_final_del_elemento)
posicion_final_del_elemento = posicion_en_lista(frutas, "mango")
print("Posición de mango = ", posicion_final_del_elemento)