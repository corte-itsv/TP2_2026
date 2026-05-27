lista_a = [8, 9, 7, 10, 6]
lista_b = [4, 5, 3, 6, 4, 5]
lista_c = []

def calcular_promedio(notas):
    cant = len(notas)
    if cant == 0:
        return 0
    return round((sum(notas) / len(notas)), 2)

print(calcular_promedio(lista_a))
print(calcular_promedio(lista_b))
print(calcular_promedio(lista_c))