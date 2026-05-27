lista_a = [8, 9, 7, 10, 6]
lista_b = [4, 5, 3, 6, 4, 5]
lista_c = []


def calcular_prom(notas):
    cant = len(notas)
    if cant == 0:
        return 0
    return sum(notas) / len(notas)
    
   
print(f'Promedio A: {calcular_prom(lista_a)}')
print(f'Promedio B: {calcular_prom(lista_b)}')
print(f'Promedio C: {calcular_prom(lista_c)}')

