def interseccion(lista_a, lista_b):
    return list(set(lista_a) & set(lista_b))

def union(lista_a, lista_b):
    return list(set(lista_a) | set(lista_b))

def solo_en_a(lista_a, lista_b):
    return list(set(lista_a) - set(lista_b))


# Prueba
clase_lunes = ["Ana", "Luis", "Sol", "Marcos", "Julia"]
clase_miercoles = ["Ana", "Sol", "Pedro", "Julia", "Tomás"]

ambos = sorted(interseccion(clase_lunes, clase_miercoles))
al_menos_uno = sorted(union(clase_lunes, clase_miercoles))
solo_lunes = sorted(solo_en_a(clase_lunes, clase_miercoles))

print("Asistieron ambos días:", ambos)
print("Asistieron al menos un día:", al_menos_uno)
print("Solo el lunes:", solo_lunes)