def interseccion(lista_a, lista_b):
   resultado = set(lista_a) & set(lista_b)
   return sorted(list(resultado))

def union(lista_a, lista_b):
    resultado = set(lista_a) | set(lista_b)
    return sorted(list(resultado))

def solo_en_a(lista_a, lista_b):
   resultado = set(lista_a) - set(lista_b)
   return sorted(list(resultado))

clase_lunes = ["Ana", "Luis", "Sol", "Marcos", "Julia"]
clase_miercoles = ["Ana", "Sol", "Pedro", "Julia", "Tomás"]

print("Asistieron ambos días:", interseccion(clase_lunes, clase_miercoles))
print("Asistieron al menos un día:", union(clase_lunes, clase_miercoles))
print("Solo el lunes:", solo_en_a(clase_lunes, clase_miercoles))
