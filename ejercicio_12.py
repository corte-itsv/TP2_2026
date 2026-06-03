def interseccion(lista_a, lista_b):
    set_b = set(lista_b)
    inter = []
    for h in lista_a:
        if h in set_b:
            inter.append(h)
            set_b.add(h)
        else:
            del h
    return sorted(inter)

def union(lista_a, lista_b):
    set_c = set(lista_a + lista_b)
    return sorted(set_c)

def solo_en_a(lista_a, lista_b):
    list_solo_a = []
    set_b = set(lista_b)
    for nombre in lista_a:
        if nombre not in set_b:
            list_solo_a.append(nombre)
    return list_solo_a

clase_lunes    = ["Ana", "Luis", "Sol", "Marcos", "Julia"]
clase_miercoles = ["Ana", "Sol", "Pedro", "Julia", "Tomás"]

print(interseccion(clase_lunes, clase_miercoles))
print(union(clase_lunes, clase_miercoles))
print(solo_en_a(clase_lunes, clase_miercoles))