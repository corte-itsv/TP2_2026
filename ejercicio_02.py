def calcular_promedio(notas):
    if len(notas) == 0:
        return 0

    promedio = sum(notas) / len(notas)
    return (promedio)


lista_a = [8, 9, 7, 10, 6]
lista_b = [4, 5, 3, 6, 4, 5]
lista_c = []

print("Promedio A:", calcular_promedio(lista_a))
print("Promedio B:", calcular_promedio(lista_b))
print("Promedio C:", calcular_promedio(lista_c))
