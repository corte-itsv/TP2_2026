def esta_en_lista(lista, elemento_a_ingresar):
    el_elemento_está = False
    for elemento in lista:
        if elemento == elemento_a_ingresar:
            el_elemento_está = True
    return el_elemento_está


def posicion_en_lista(lista, elemento_a_ingresar):
    existencia = esta_en_lista(lista, elemento_a_ingresar)
    posicion_del_elemento = 0
    if existencia == True:
        for elemento in lista:
            if elemento == elemento_a_ingresar:
                return posicion_del_elemento
            else:
                posicion_del_elemento = posicion_del_elemento + 1
    else:
        posicion_del_elemento = "-1"



frutas = ["manzana", "banana", "pera", "uva", "kiwi"]



print("================= ¿EXISTE? ==================")

el_elemento_está = esta_en_lista(frutas, "pera")
print("¿El elemento 'pera' está en la lista? :", el_elemento_está)

el_elemento_está = esta_en_lista(frutas, "mango")
print("¿El elemento 'mango' está en la lista? :", el_elemento_está)

print("")


print("================ ¿DÓNDE ESTÁ? ================")

posicion_del_elemento = posicion_en_lista(frutas, "uva")
print("Posición del elemento 'uva':", posicion_del_elemento)

posicion_del_elemento = posicion_en_lista(frutas, "mango")
print("Posición del elemento 'mango':", posicion_del_elemento)