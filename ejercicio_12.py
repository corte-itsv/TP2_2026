def interseccion(lista_a, lista_b):
    a = set(lista_a)
    b = set(lista_b)
    return list(a.intersection(b))

def union(lista_a, lista_b):
    a = set(lista_a)
    b = set(lista_b)
    return list(a.union(b))

def solo_en_a(lista_a, lista_b):
    a = set(lista_a)
    b = set(lista_b)
    return list(a.difference(b))

clase_lunes    = ["Ana", "Luis", "Sol", "Marcos", "Julia"]
clase_miercoles = ["Ana", "Sol", "Pedro", "Julia", "Tomás"]

print(interseccion(clase_lunes, clase_miercoles))
print(union(clase_lunes, clase_miercoles))
print(solo_en_a(clase_lunes, clase_miercoles))