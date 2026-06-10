def interseccion(lista_a, lista_b):
    dos = set(lista_a) & set(lista_b)
    return sorted(dos)
    
def union(lista_a, lista_b):
    unionf = set(lista_a) | set(lista_b)
    return sorted(unionf)

def solo_en_a(lista_a, lista_b):
    dif = set(lista_a) - set(lista_b)
    return sorted(dif)
clase_lunes    = ["Ana", "Luis", "Sol", "Marcos", "Julia"]
clase_miercoles = ["Ana", "Sol", "Pedro", "Julia", "Tomás"]

print(f"Asistieron ambos días: {interseccion(clase_lunes, clase_miercoles)}")
print(f"Asistieron al menos un día: {union(clase_lunes, clase_miercoles)}")
print(f"Solo el lunes: {solo_en_a(clase_lunes, clase_miercoles)}")