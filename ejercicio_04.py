def min_max(numeros):
    minimo = numeros[0]
    maximo = numeros[0]
    
    for num in numeros:
        if num < minimo:
            minimo = num 
        if num > maximo:
            maximo = num
    return minimo, maximo
    
lista_numeros = [34, 7, 89, 12, 56, 3, 78, 45]
min_num, max_num = min_max(lista_numeros)
print(f'Minimo: {min_num}')
print(f'Minimo: {max_num}')
