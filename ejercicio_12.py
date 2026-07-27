def interseccion(lista_a, lista_b):
    lista_solo_los_que_estan_en_a_b = []
    for elemento_a in lista_a:
        for elemento_b in lista_b:
            if elemento_a == elemento_b:
                lista_solo_los_que_estan_en_a_b.append(elemento_a)
    return lista_solo_los_que_estan_en_a_b

def union(lista_a, lista_b):
    set_lista = set()
    lista_a_b = []
    for elemento_a in lista_a:
        for elemento_b in lista_b:
            if elemento_a not in set_lista:
                set_lista.add(elemento_a)
                lista_a_b.append(elemento_a)
            if elemento_b not in set_lista:
                set_lista.add(elemento_b)
                lista_a_b.append(elemento_b)
    return lista_a_b

def solo_en_a(lista_a, lista_b):
    set_lista = set()
    elementos_de_a_que_no_estan_en_b = []
    for elemento_a in lista_a:
            if elemento_a not in lista_b:
                set_lista.add(elemento_a)
                elementos_de_a_que_no_estan_en_b.append(elemento_a)
    return elementos_de_a_que_no_estan_en_b

clase_lunes    = ["Ana", "Luis", "Sol", "Marcos", "Julia"]
clase_miercoles = ["Ana", "Sol", "Pedro", "Julia", "Tomás"]

print("============== INTERSECCION ==============")

lista_solo_los_que_estan_en_a_b = interseccion(clase_lunes, clase_miercoles)
print("Asistieron ambos días:")
print(lista_solo_los_que_estan_en_a_b)
print("")

print("================= UNIÓN ==================")

listas_unidas = union(clase_lunes, clase_miercoles)
print("Asistieron al menos un día:")
print(listas_unidas)
print("")

print("================ EXCLUCIÓN ===============")

elementos_de_a_que_no_estan_en_b = solo_en_a(clase_lunes, clase_miercoles)
print("Solo el lunes:")
print(elementos_de_a_que_no_estan_en_b)