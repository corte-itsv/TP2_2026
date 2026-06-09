def interseccion(lista_a, lista_b):
    resultado = []
    for elemento in lista_a:
        if elemento in lista_b and elemento not in resultado:
            resultado.append(elemento)
    return resultado 


def union(lista_a, lista_b):
    resultado = lista_a.copy()
    for elemento in lista_b:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado 


def solo_en_a(lista_a, lista_b):
    resultado = []
    for elemento in lista_a:
        if elemento not in lista_b and elemento not in resultado:
            resultado.append(elemento)
    return resultado 


clase_lunes    = ["Ana", "Luis", "Sol", "Marcos", "Julia"]
clase_miercoles = ["Ana", "Sol", "Pedro", "Julia", "Tomás"]


print("Asistieron ambos días:", interseccion(clase_lunes, clase_miercoles))
print("Asistieron al menos un día:", union(clase_lunes, clase_miercoles))
print("Solo el lunes:", solo_en_a(clase_lunes, clase_miercoles))