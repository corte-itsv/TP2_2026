def length(notas): 
    cantidad_elementos_notas = len(notas)
    if cantidad_elementos_notas == 0:
        return 0
    cantidad = 0
    for nota in notas:
        cantidad = cantidad + 1
    return cantidad
    
def suma(notas): 
    suma_total = 0
    for nota in notas:
        suma_total = suma_total + nota
    return suma_total

def calcular_promedio(notas): 
    cantidad_elementos_notas = length(notas)
    if cantidad_elementos_notas == 0:
        return 0
    suma_total = suma(notas)
    promedio_calculado = suma_total / cantidad_elementos_notas
    return  promedio_calculado

lista_a = [8, 9, 7, 10, 6]
lista_b = [4, 5, 3, 6, 4, 5]
lista_c = []

promedio_a = calcular_promedio(lista_a)
print("Promedio A: ", promedio_a)
promedio_b = calcular_promedio(lista_b)
print("Promedio B: ", promedio_b)
promedio_c = calcular_promedio(lista_c)
print("Promedio C: ", promedio_c)