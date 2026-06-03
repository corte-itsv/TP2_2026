def calcular_promedio(notas):
 if not notas:
    return 0
 else:    
    return round(sum(notas) / len(notas), 2)

lista_a = [8, 9, 7, 10, 6]
print(f"Promedio A: {calcular_promedio(lista_a)}")
lista_b = [4, 5, 3, 6, 4, 5]
print(f"Promedio B: {calcular_promedio(lista_b)}")
lista_c = []
print(f"Promedio C: {calcular_promedio(lista_c)}") 