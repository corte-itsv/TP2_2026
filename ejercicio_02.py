def calcular_promedio(notas):
    suma = 0
    cant = 0
    promedio = 0
    for nota in notas:
        cant += 1
        suma += nota
        promedio = suma/cant
    print(promedio)
lista_a = [8, 9, 7, 10, 6]
lista_b = [4, 5, 3, 6, 4, 5]
lista_c = []
calcular_promedio(lista_a)
calcular_promedio(lista_b)
calcular_promedio(lista_c)
