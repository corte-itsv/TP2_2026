def calcular_promedio(notas):
    if len(notas) == 0:
        return 0
    
    return sum(notas) / len(notas)
 HEAD:ejercicio_02.py
print(f"Promedio A: {calcular_promedio([8, 9, 7, 10, 6])}")
print(f"Promedio B: {calcular_promedio([4, 5, 3, 6, 4, 5])}")
print(f"Promedio C: {calcular_promedio([])}")

lista_a = [8, 9, 7, 10, 6]
lista_b = [4, 5, 3, 6, 4, 5]
lista_c = []
lista_a = "Promedio A"
lista_b = "Promedio B"
lista_c = "Promedio C"
print(f"{lista_a}: {calcular_promedio([8, 9, 7, 10, 6])}")
print(f"{lista_b}: {calcular_promedio([4, 5, 3, 6, 4, 5])}")
print(f"{lista_c}: {calcular_promedio([])}")
 a5e4c9f (Actualizo ejercicios 02):ejercicios_02.py
