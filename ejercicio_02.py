def calcular_promedio(notas):
    promedio_de_notas = 0
    suma_total = 0
    for nota in notas:
        suma_total = suma_total + nota
    if suma_total > 0:
        promedio_de_notas = suma_total / len(notas)
        promedio_final = round(promedio_de_notas, 2)
    else:
        promedio_final = 0
        
    return promedio_final


lista_a = [8, 9, 7, 10, 6]
lista_b = [4, 5, 3, 6, 4, 5]
lista_c = []

print("=== PROMEDIOS ===")

promedio_lista_a = calcular_promedio(lista_a)
print("Promedio: ", promedio_lista_a)
promedio_lista_b = calcular_promedio(lista_b)
print("Promedio: ", promedio_lista_b)
promedio_lista_c = calcular_promedio(lista_c)
print("Promedio: ", promedio_lista_c)
