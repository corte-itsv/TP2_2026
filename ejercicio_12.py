def interseccion(lista_a, lista_b):

    return (list(set(lista_a) & set(lista_b)))

def union(lista_a, lista_b):

    return (list(set(lista_a) | set(lista_b)))
    

def solo_en_a(lista_a, lista_b):

    return list(set(lista_a) - set(lista_b))

clase_lunes    = ["Ana", "Luis", "Sol", "Marcos", "Julia"]
clase_miercoles = ["Ana", "Sol", "Pedro", "Julia", "Tomás"]

print(f'Asistieron ambos días: {sorted(interseccion(clase_lunes, clase_miercoles))}')
print(f'Asistieron al menos un día: {sorted(union(clase_lunes, clase_miercoles))}')
print(f'Solo el lunes: {sorted(solo_en_a(clase_lunes, clase_miercoles))}')