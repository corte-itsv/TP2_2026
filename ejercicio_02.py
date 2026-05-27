def calcular_promedio(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

A = [8, 9, 7, 10, 6]
B = [4, 5, 3, 6, 4, 5]
C = []
nombres = ["A", "B", "C"]

for i, notas in enumerate([A, B, C]):
    promedio = calcular_promedio(notas)
    print(f"promedio {nombres[i]}: {promedio}")
    

