lista_a = [8, 9, 7, 10, 6]
lista_b = [4, 5, 3, 6, 4, 5]
lista_c = []
def calcular_promedios(notas):
    cant = len(notas)
    if cant == 0:
        return 0
    return sum(notas) / len(notas)
print(calcular_promedios(lista_a))
print(calcular_promedios(lista_b))
print(calcular_promedios(lista_c))