def calcular_promedio(notas):
    if not notas:
        return 0
    promedio = sum(notas) / len(notas)
    return round(promedio, 2) 

lista_a = [8, 9, 7, 10, 6]
lista_b = [4, 5, 3, 6, 4, 5]
lista_c = []

print(f"Promedio de lista_a = {calcular_promedio(lista_a)}")
print(f"Promedio de lista_b = {calcular_promedio(lista_b)}") 
print(f"Promedio de lista_c = {calcular_promedio(lista_c)}")
