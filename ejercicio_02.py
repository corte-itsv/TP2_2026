def calcular_promedio(notas):
    if len(notas) == 0:
        return 0
    
    return sum(notas) / len(notas)
print(f"Promedio A: {calcular_promedio([8, 9, 7, 10, 6])}")
print(f"Promedio B: {calcular_promedio([4, 5, 3, 6, 4, 5])}")
print(f"Promedio C: {calcular_promedio([])}")
