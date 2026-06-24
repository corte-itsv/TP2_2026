def agrupar_por_inicial(nombres):
    diccionario = {}
    for nombre_prim_for in nombres:
        primera_letra_nombre_prim_for = nombre_prim_for[0].upper()
        diccionario[primera_letra_nombre_prim_for] = [nombre_prim_for]
        for nombre_seg_for in nombres:
            primera_letra_nombre_seg_for = nombre_seg_for[0].upper()
            if primera_letra_nombre_seg_for == primera_letra_nombre_prim_for and nombre_seg_for not in diccionario[primera_letra_nombre_prim_for]:
                diccionario[primera_letra_nombre_prim_for].append(nombre_seg_for) 
    return diccionario

def mostrar(diccionario):
    for primer_letra_nombre, nombres_etc in diccionario.items():
        print(primer_letra_nombre, ": ", nombres_etc)
        


lista_de_nombres = ["Ana", "Alberto", "Belen", "Bruno", "Carlos", "Camila", "Ana Paula", "Diego", "Daniela"]


diccionario_final = agrupar_por_inicial(lista_de_nombres)
# print(diccionario_final)

mostrar(diccionario_final)