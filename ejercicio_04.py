def min_max(numeros):
    maximo = numeros[0]
    for numero in numeros:
        if numero > maximo:
            maximo = numero
        minimo = numeros[0]
    for numero in numeros:
        if numero < minimo:
            minimo = numero
    return minimo, maximo
    
numeros = [34, 7, 89, 12, 56, 3, 78, 45]

minimo, maximo = min_max(numeros)
print(f"Mínimo: {minimo}")
print(f"Máximo: {maximo}")
