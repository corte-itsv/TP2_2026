lista_a = [8, 9, 7, 10, 6]
lista_b = [4, 5, 3, 6, 4, 5]
lista_c = []

def calcular_promedio(notas):
    cant = len(notas)
    if cant == 0:
        return 0
    return sum(notas) / len(notas)

print(round(calcular_promedio(lista_a), 2))
print(round(calcular_promedio(lista_b), 2))
print(round(calcular_promedio(lista_c), 2))