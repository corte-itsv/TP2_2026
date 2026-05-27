def calcular_promedio(notas):    
    if len(notas) == 0:
        return (0)
    suma_total = 0
    for nota in notas:
        suma_total += nota
    cantidad_notas = len(notas)
    promedio = suma_total / cantidad_notas
    return round(promedio, 2)

lista_a = [8, 9, 7, 10, 6]
lista_b = [4, 5, 3, 6, 4, 5]
lista_c = []

print(f"Promedio A: {calcular_promedio(lista_a)}")
print(f"Promedio B: {calcular_promedio(lista_b)}")
print(f"Promedio C: {calcular_promedio(lista_c)}")

  