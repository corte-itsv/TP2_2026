def interseccion(lista_a, lista_b):
    set_a=set(lista_a)
    set_b=set(lista_b)
    return sorted(set_a & set_b)    

def union(lista_a, lista_b):
    set_a=set(lista_a)
    set_b=set(lista_b)
    return sorted(set_a | set_b)
    
def solo_en_a(lista_a, lista_b):
    set_a=set(lista_a)
    set_b=set(lista_b)
    return sorted(set_a - set_b)

clase_lunes    = ["Ana", "Luis", "Sol", "Marcos", "Julia"]
clase_miercoles = ["Ana", "Sol", "Pedro", "Julia", "Tomás"]
print(f"Asistieron en ambos dias: {interseccion(clase_lunes, clase_miercoles)}")
print(f"Asistieron al menos un dia:{union(clase_lunes, clase_miercoles)}")
print(f"Solo el lunes:{solo_en_a(clase_lunes, clase_miercoles)}")