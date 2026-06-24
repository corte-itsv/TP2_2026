def interseccion(lista_a, lista_b):
    set_lista = set()
    lista_final = []
    for elemento_lista_a in lista_a:
        for elemento_lista_b in lista_b:
            if elemento_lista_a == elemento_lista_b and elemento_lista_a not in set_lista:
                set_lista.add(elemento_lista_a)
                lista_final.append(elemento_lista_a)
        
    return lista_final

def union(lista_a, lista_b):
    set_lista = set()
    lista_final = []
    for elemento_lista_a in lista_a:
        if elemento_lista_a not in set_lista:
            set_lista.add(elemento_lista_a)
            lista_final.append(elemento_lista_a)
    for elemento_lista_b in lista_b:
        if elemento_lista_b not in set_lista:
            set_lista.add(elemento_lista_b)
            lista_final.append(elemento_lista_b)
    return lista_final
    
def solo_en_a(lista_a, lista_b):
    set_lista_b = set(lista_b)
    lista_final = []
    for elemento_lista_a in lista_a:
        if elemento_lista_a not in set_lista_b:
            lista_final.append(elemento_lista_a)
    return lista_final
    
    
clase_lunes    = ["Ana", "Luis", "Sol", "Marcos", "Julia"]
clase_miercoles = ["Ana", "Sol", "Pedro", "Julia", "Tomás"]

lista_interseccionada = interseccion(clase_lunes, clase_miercoles)
print("Asistieron ambos días: ", lista_interseccionada)

lista_unida = union(clase_lunes, clase_miercoles)
print("Asistieron al menos un día: ", lista_unida)

contenido_de_lista_a = solo_en_a(clase_lunes, clase_miercoles)
print("Solo el lunes: ", contenido_de_lista_a)
