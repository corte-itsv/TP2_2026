def min_max(numeros):
    minimo = numeros[0]
    maximo = numeros[0]

    for numero in numeros:
        if numero < minimo:
            minimo = numero
            
        if numero > maximo:
            maximo = numero
    
    return minimo, maximo

numeros = [34, 7, 89, 12, 56, 3, 78, 45]

minimo, maximo = min_max(numeros)

print("Minimo:", minimo)
print("Maximo:", maximo)