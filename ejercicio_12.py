def interseccion(lista_a, lista_b):
    return list(set(lista_b) & set(lista_a))

def solo_en_a(lista_a, lista_b):
    return list(set(lista_a) - set(lista_b))

def union(lista_a, lista_b):
    return list(set(lista_a) | set(lista_b))

clase_lunes    = ["Ana", "Luis", "Sol", "Marcos", "Julia"]
clase_miercoles = ["Ana", "Sol", "Pedro", "Julia", "Tomás"]

ambos = interseccion(clase_lunes, clase_miercoles)
solo_a = solo_en_a(clase_lunes, clase_miercoles)
unite = union(clase_lunes, clase_miercoles) 

print(f"Asistieron ambos días: {sorted(ambos)}")
print(f"Asistieron al menos un día: {sorted(unite)}")
print(f"Solo el lunes: {sorted(solo_a)}")