def min_max(numeros):
    minimo = numeros[0]
    maximo = numeros[0]
    
    for numero in numeros:
        if numero < minimo:
            minimo = numero
        if numero > maximo:
            maximo = numero
    
    return (minimo, maximo)
numeros = [34, 7, 89, 12, 56, 3, 78, 45]
resultado = min_max(numeros)

minimo, maximo = resultado

print(f"Lista: {numeros}")
print(f"Valor mínimo: {minimo}")
print(f"Valor máximo: {maximo}")
